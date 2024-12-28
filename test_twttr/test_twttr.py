from twttr import shorten

def test_lower():
    assert shorten("twitter") == "twttr"

def test_upper():
    assert shorten("HELLO, WORLD") == "HLL, WRLD"

def test_upperlower():
    assert shorten("HeLlo, ChihEB") == "HLl, ChhB"

def test_number():
    assert shorten("5554446666666") == "5554446666666"

def test_mix():
    assert shorten ("!!!?? helLo, Cs50 EeEff") == "!!!?? hlL, Cs50 ff"
