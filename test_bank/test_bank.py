from bank import value


def test_lowerupper ():
    assert value("hola") == 20
    assert value("HOLA") == 20
    assert value("HELLO SNIOR") == 0

def test_helo():
    assert value("hello sinior") == 0
    assert value("sinior hello") == 100
    assert value("!!!hello sinior!!!") == 100




def test_nogreeting():
    assert value("give me my money") == 100
