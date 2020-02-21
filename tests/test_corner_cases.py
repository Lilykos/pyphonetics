import pytest
from pyphonetics import Soundex, RefinedSoundex, FuzzySoundex
from pyphonetics.exceptions import EmptyStringError


def test_soundex():
    soundex = Soundex()

    assert soundex.phonetics('h') == 'H000'
    assert soundex.phonetics('d') == 'D000'

    with pytest.raises(EmptyStringError):
        soundex.phonetics('')


def test_refined_soundex():
    soundex = RefinedSoundex()

    assert soundex.phonetics('h') == 'H'
    assert soundex.phonetics('d') == 'D6'

    with pytest.raises(EmptyStringError):
        soundex.phonetics('')


def test_fuzzy_soundex():
    soundex = FuzzySoundex()

    with pytest.raises(EmptyStringError):
        soundex.phonetics('')
