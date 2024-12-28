from plates import is_valid


def test_length():
    assert is_valid("helloworld") == False
    assert is_valid("h") == False


def test_number():
    assert is_valid("50cs") == False
    assert is_valid("5000") == False
    assert is_valid ("cs50") == True
    assert is_valid ("tst055") == False
    assert is_valid("cs50cs") == False
    assert is_valid ("yo77") == True

def test_lowerupper():
    assert is_valid ("HLlo50") == True
    assert is_valid ("wOrLd") == True

def test_alphanum():
    assert is_valid("tst-5") == False
    assert is_valid("cs!!") == False
    assert is_valid("!$$$11") == False
