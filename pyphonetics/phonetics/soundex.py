import re
from unidecode import unidecode

from ..utils import translation, squeeze
from ..exceptions import UnicodeException
from .phonetic_algorithm import PhoneticAlgorithm


class Soundex(PhoneticAlgorithm):
    """
    The Soundex algorithm.

    [Reference]: https://en.wikipedia.org/wiki/Soundex
    [Authors]: Robert C. Russel, Margaret King Odell
    """
    def __init__(self, refined=False):
        self.translations = translation(
            'AEIOUYWHBPFVCSKGJQXZDTLMNR',
            '000000DD111122222222334556'
        )

        self.refined_translations = translation(
            'AEIOUYWHBPFVCKSGJQXZDTLMNR',
            '000000DD112233344555667889'
        )

        self.refined = refined
        self.pad = lambda code: '{}0000'.format(code)[:4]

    def phonetics(self, word):
        if not isinstance(word, str):
            raise UnicodeException('Expected a unicode string!')

        word = unidecode(word).upper()
        word = re.sub(r'[^A-Z]', r'', word)

        first_letter = word[0]

        if self.refined:
            return self._refined_soundex(first_letter, word)
        else:
            return self._soundex(first_letter, word)

    #
    # Private methods Simple/Refined Soundex
    #
    def _soundex(self, first_letter, word):
        """Soundex algorithm."""
        tail = ''.join(self.translations[char]
                       for char in word
                       if self.translations[char] != 'D')

        # Dropping first code's letter if duplicate
        if tail[0] == self.translations[first_letter]:
            tail = tail[1:]

        code = squeeze(tail).replace('0', '')
        return self.pad(first_letter + code)

    def _refined_soundex(self, first_letter, word):
        """Refined Soundex algorithm."""
        tail = ''.join(self.refined_translations[char]
                       for char in word
                       if self.refined_translations[char] != 'D')
        code = squeeze(tail)
        return first_letter + code
