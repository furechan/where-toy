from where import where_module


def test_where():
    res = where_module("sys")
    assert res is not None

    res = where_module("abcdefg")
    assert res is None

