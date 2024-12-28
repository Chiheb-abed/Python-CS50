from jar import Jar
import pytest


def test_init():
    jar=Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    jar = Jar(4)
    assert jar.capacity == 4




def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        assert jar.deposit(13) == ValueError
        assert jar.deposit(-2) == ValueError
        assert jar.deposit(0) == ValueError


def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        assert jar.deposit(13) == ValueError
    jar.deposit(5)
    assert jar.size == 5
    jar.withdraw(2)
    assert jar.size == 3
    with pytest.raises(ValueError):
        assert jar.withdraw(13) == ValueError
        assert jar.withdraw(-2) == ValueError
        assert jar.withdraw(0) == ValueError
