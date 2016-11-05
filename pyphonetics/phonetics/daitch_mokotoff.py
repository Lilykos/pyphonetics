import re
from unidecode import unidecode

from ..exceptions import UnicodeException
from .phonetic_algorithm import PhoneticAlgorithm


class DaitchMokotoff(PhoneticAlgorithm):
    """
    The Daitch-Mokotoff Soundex.

    [Reference]: https://en.wikipedia.org/wiki/Daitch%E2%80%93Mokotoff_Soundex
    [Note]: For the (RS|RZ) part, the original algo says (94, 4) but most implementations
        drop it to only (94). This implementation follows the original algo.
    """
    def __init__(self):
        self.rules = {
            'A': [
                [r'^(AI|AJ|AY)', 0, 1, None],
                [r'^AU', 0, 7, None],
                [None, 0, None, None]
            ],
            'Ą': [
                [None, None, None, [6, None]]
            ],
            'B': [
                [None, 7, 7, 7]
            ],
            'C': [
                [r'^CHS', 5, 54, 54],
                [r'^CH', [5, 4], [5, 4], [5, 4]],
                [r'^CK', [5, 45], [5, 45], [5, 45]],
                [r'^(CSZ|CZS|CZ|CS)', 4, 4, 4],
                [None, [5, 4], [5, 4], [5, 4]]
            ],
            'D': [
                [r'^(DRZ|DRS|DSH|DSZ|DZH|DZS|DS|DZ)', 4, 4, 4],
                [r'^(DT|D)', 3, 3, 3]
            ],
            'E': [
                [r'^(EI|EJ|EY)', 0, 1, None],
                [r'^EU', 1, 1, None],
                [None, 0, None, None],
            ],
            'Ę': [
                [None, None, None, [6, None]]
            ],
            'F': [
                [r'^(FB|F)', 7, 7, 7]
            ],
            'G': [
                [None, 5, 5, 5]
            ],
            'H': [
                [None, 5, 5, None]
            ],
            'I': [
                [r'^(IA|IE|IO|IU)', 1, None, None],
                [None, 0, None, None]
            ],
            'J': [
                [None, [1, 4], [None, 4], [None, 4]]
            ],
            'K': [
                [r'^KS', 5, 54, 54],
                [r'^(KH|K)', 5, 5, 5]
            ],
            'L': [
                [None, 8, 8, 8]
            ],
            'M': [
                ['MNNM', None, 66, 66],
                ['MN', 6, 6, 6]
            ],
            'N': [
                ['MNNM', None, 66, 66],
                ['MN', 6, 6, 6],
            ],
            'O': [
                [r'^(OI|OJ|OY)', 0, 1, None],
                [None, 0, None, None]
            ],
            'P': [
                [r'^(PF|PH|P)', 7, 7, 7]
            ],
            'Q': [
                [None, 5, 5, 5]
            ],
            'R': [
                [r'^(RZ|RS)', [94, 4], [94, 4], [94, 4]],
                [None, 9, 9, 9]
            ],
            'S': [
                [r'^(SCHTSCH|SCHTSH|SCHTCH|SHTCH|SHCH|SHTSH)', 2, 4, 4],
                [r'^SCH', 4, 4, 4],
                [r'^(SHT|SCHT|SCHD)', 2, 43, 43],
                [r'^SH', 4, 4, 4],
                [r'^(STCH|STSCH|SC|STRZ|STRS|STSH)', 2, 4, 4],
                [r'^ST', 2, 43, 43],
                [r'^(SZCZ|SZCS)', 2, 4, 4],
                [r'^(SZT|SHD|SZD|SD)', 2, 43, 43],
                [r'^(SZ|S)', 4, 4, 4]
            ],
            'T': [
                [r'^(TCH|TTCH|TTSCH)', 4, 4, 4],
                [r'^TH', 3, 3, 3],
                [r'^(TRZ|TRS|TSCH|TSH|TS|TTS|TTSZ|TC|TZ|TTZ|TZS|TSZ)', 4, 4, 4],
                [None, 3, 3, 3]
            ],
            'Ţ': [
                [None, [3, 4], [3, 4], [3, 4]]
            ],
            'U': [
                [r'^(UI|UJ|UY)', 0, 1, None],
                [r'^(UE|U)', 0, None, None]
            ],
            'V': [
                [None, 7, 7, 7]
            ],
            'W': [
                [None, 7, 7, 7]
            ],
            'X': [
                [None, 5, 54, 54]
            ],
            'Y': [
                [None, 1, None, None]
            ],
            'Z': [
                [r'^(ZHDZH|ZDZH|ZDZ)', 2, 4, 4],
                [r'^(ZHD|ZD)', 2, 43, 43],
                [r'^(ZSCH|ZSH|ZH|ZS|Z)', 4, 4, 4]
            ],
        }
        self.pad = lambda code: '{}000000'.format(code)[:6]
        self.vowels = 'AEIOUY'

    def _permutations(self, code):
        codes = ['']

        for current_part in code:

            if isinstance(current_part, dict):
                # Double the codes
                for item in codes:
                    codes.append(item)

                # Fill the nodes
                length = len(codes)
                for i in range(length):
                    s = current_part[0] if i < length/2 else current_part[1]
                    codes[i] = codes[i] + s if s is not None else codes[i]

            else:
                for i in range(len(codes)):
                    codes[i] += current_part

    def phonetics(self, word):
        if not isinstance(word, str):
            raise UnicodeException('Expected a unicode string!')

        code = []
        word = unidecode(word).upper()
        current = re.sub(r'[^A-ZĄĘŢ]', r'', word)

        start = True
        last_pattern = ''

        while len(current):
            first_letter = current[0]
            rules = self.rules[first_letter]

            for rule in rules:
                pattern, if_first_letter,\
                    vowel_next, usual = rule

                match = re.match(pattern, current) if pattern else [first_letter]
                if match:
                    if isinstance(match, list):
                        offset = len(match[0])
                    else:
                        offset = len(pattern)

                    correct_code = usual

                    if start:
                        correct_code = if_first_letter
                    elif current[offset] in self.vowels:
                        correct_code = vowel_next

                    if last_pattern != pattern and correct_code is not None:
                        code.append(correct_code)

                    last_pattern = pattern or first_letter
                    current = current[offset:]
                    break

            start = False

        return map(self.pad, self._permutations(code))

