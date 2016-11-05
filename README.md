# Pyphonetics

Pyphonetics is a Python 3 library for phonetic algorithms. Right now, the following algorithms are implemented and supported:

 * Soundex
 * Metaphone
 * Refined Soundex
 * Fuzzy Soundex
 * Lein
 * Matching Rating Approach

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

## Credits

The module was largely based on the implementation of phonetic algorithms found in the [Talisman.js](https://github.com/Yomguithereal/talisman) Node NLP library.