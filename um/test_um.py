from um import count


def test_insidestring():
    assert count("yummy") == 0
    assert count("chumy") == 0
    assert count ("dumydumy is chumy chumy") == 0

def test_start():
    assert count ("um") == 1
    assert count ("um hummm hello world") == 1

def test_multi():
    assert count ("um hello, um, world") == 2
    assert count("um hello, um, world, um") == 3
    assert count("hello um5, world") == 0
    assert count("hello, um , world, um?")== 2


def test_caseins():
    assert count ("Um") == 1
    assert count ("UM hello Um world , um") == 3
