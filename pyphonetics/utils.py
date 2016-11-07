from itertools import groupby

from .exceptions import WrongLengthException


def translation(first, second):
    """Create an index of mapped letters (zip to dict)."""
    if len(first) != len(second):
        raise WrongLengthException('The lists are not of the same length!')
    return dict(zip(first, second))


def squeeze(word):
    """Squeeze the given sequence by dropping consecutive duplicates."""
    return ''.join(x[0] for x in groupby(word))
