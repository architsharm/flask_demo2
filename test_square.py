from square import get_square


def test_get_square():
    a=4
    res=get_square(a)
    assert res==16
