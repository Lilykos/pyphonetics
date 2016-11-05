from pyphonetics.utils import squeeze, translation


def test_squeeze():
    tests = [
        ('test', 'test'),
        ('hello yellow', 'helo yelow'),
        ('112345566', '123456')
    ]

    for test in tests:
        assert squeeze(test[0]) == test[1]


def test_translation():
    assert translation(['a', 'b', 'c'], [1, 2, 3]) == {'a': 1, 'b': 2, 'c': 3}
