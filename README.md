# Pyphonetics

Pyphonetics is a Python 3 library for phonetic algorithms. Right now, the following algorithms are implemented and supported:

 * Soundex
 * Metaphone
 * Refined Soundex
 * Fuzzy Soundex
 * Lein
 * Matching Rating Approach
 
In addition, the following distance metrics:

 * Hamming
 * Levenshtein

More will be added in the future.

## Instalation

The module is available in PyPI, just use `pip install pyphonetics`.


## Usage

```python
>>> from pyphonetics import Soundex
>>> soundex = Soundex()
>>> soundex.phonetics('Rupert')
'R163'
>>> soundex.phonetics('Robert')
'R163'
>>> soundex.sounds_like('Robert', 'Rupert')
True
```

The same API applies to every algorithm, e.g:

```python
>>> from pyphonetics import Metaphone
>>> metaphone = Metaphone()
>>> metaphone.phonetics('discrimination')
'TSKRMNXN'
```

You can also use the `distance(word1, word2, metric='levenshtein')` method to find the distance between 2 phonetic representations.

```python
>>> from pyphonetics import RefinedSoundex
>>> rs = RefinedSoundex()
>>> rs.distance('Rupert', 'Robert')
0
>>> rs.distance('assign', 'assist', metric='hamming')
2
```

## Credits

The module was largely based on the implementation of phonetic algorithms found in the [Talisman.js](https://github.com/Yomguithereal/talisman) Node NLP library.