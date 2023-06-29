from helloFunction import hello


def test_default():
    assert hello() == "hello, world"


def test_arguement():
    assert hello("Sravan") == "hello, Sravan"
