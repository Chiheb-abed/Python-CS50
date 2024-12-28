from fuel import convert
from fuel import gauge
import pytest



def test_convert ():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    assert convert("4/5") == 80
    assert convert("1/8") == 12

def test_gauge():
    assert  gauge(80) == "80%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"


