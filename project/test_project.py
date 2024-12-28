from project import fight,Character,fight_round,show_item,Item
import pytest


def test_fight():
    dummy=Character("dummy",health=10)
    player=Character("p")
    inventory=[]
    dummy2=Character("dummy",health=1000)
    assert fight(player,dummy,inventory)=="you won"
    with pytest.raises(SystemExit) as sample:
        fight(player,dummy2,inventory)
    assert sample.type == SystemExit
    assert sample.value.code == 'Game Over'


def test_fight_round():
    player=Character("test",strength=0)
    dummy=Character("testdummy")
    for i in range(10):
        assert fight_round(dummy,player) == 0
        assert fight_round(player,dummy) in [0,1,2,3,4,5]

def test_show_item():
    dagger = Item("God of thunder", 1, 1, "weapon")
    healing_potion = Item("Healing Potion", 1, 20, "potion")
    inv = []
    inv.append(dagger)
    assert show_item(inv) == "item 1 :  Item Name: God of thunder  Item durability: 1\n"
    inv.append(healing_potion)
    assert show_item(inv) == "item 1 :  Item Name: God of thunder  Item durability: 1\nitem 2 :  Item Name: Healing Potion  Item durability: 1\n"







