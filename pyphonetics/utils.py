from itertools import groupby

from .exceptions import WrongLengthException


def translation(first, second):
    """Create an index of mapped letters (zip to dict)."""
    if len(first) != len(second):
        raise WrongLengthException('Expected a unicode string!')
    return dict(zip(first, second))


def squeeze(word):
    """squeeze the given sequence by dropping consecutive duplicates."""
    return ''.join(x[0] for x in groupby(word))
