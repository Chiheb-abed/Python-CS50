from numb3rs import validate

def test_coorectINP ():
    assert validate("255.255.255.255") == True
    assert validate ("1.2.5.4") == True
    assert validate ("20.25.30.14") == True
    assert validate ("1.25.0.255") ==True


def test_incorrectINP():
    assert validate("cat") == False
    assert validate ("cat.dog.cat.dog")== False
    assert validate ("256.256.256.256") == False
    assert validate ("2")== False
    assert validate ("2.2.2")== False
    assert validate ("20.255.120.300")== False
    assert validate ("20.255.120.255.200")== False


