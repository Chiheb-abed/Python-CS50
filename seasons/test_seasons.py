from seasons import dates

def test_error():
    assert dates.checkdate("22222") == False
    assert dates.checkdate("20021212") == False
    assert dates.checkdate("2000/12/11") == False
    assert dates.checkdate("march , 28 1993") == False
