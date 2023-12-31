from where import where_module

def test_where():
    res = where_module("where")
    assert res is not None

