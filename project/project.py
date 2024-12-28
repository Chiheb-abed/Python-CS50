import sys
from rich.console import Console
from rich.table import Table
import csv
from pyfiglet import Figlet
import time
import random


import os


class Character:
    def __init__(self, name, health=100, mana=0, strength=5, gold=0, max_health=100):
        self.name = name
        self.health = health
        self.mana = mana
        self.strength = strength
        self.gold = gold
        self.max_health = max_health

    def __str__(self):
        return f"Name: {self.name}\n Health: {self.health}\n Mana:{self.mana}\n Armor:{self.armor}\n Gold:{self.gold}\n"

    @classmethod
    def get_name(cls):
        while True:
            name = input("waht is you character name: ").upper()
            if name:
                return cls(name)
            else:
                print("you need to enter a valid name.")


class Item:
    def __init__(self, name, durability, attack, type):
        self.durability = int(durability)
        self.name = name
        self.attack = int(attack)
        self.type = type

    @classmethod
    def use_weapon(cls, item, inventory):
        if item.durability - 1 > 0:
            item.durability -= 1
            return item.durability
        else:
            Item.destroy(item, inventory)

    @classmethod
    def use_potion(cls, item, player, inventory):
        if item.attack + player.health < player.max_health:
            player.health += item.attack
        else:
            player.health = player.max_health
        item.destroy(item, inventory)

    @classmethod
    def destroy(cls, item, inventory):

        print(f"{item.name} have been destroyed")
        inventory.remove(item)

    def __str__(self):
        return f" Item Name: {self.name}  Item durability: {self.durability}"


def main():
    inventory = []
    # setup
    f = Figlet(font='big')
    list = [4, 1, 2, 2, 1,2,4,5]
    lin_nbr = 0
    row_nbr = 1
    i = 0
    player = Character.get_name()
    clear_terminal()
    print(f.renderText(f"Welcome {player.name}"))
    time.sleep(2)
    clear_terminal()
    print(f.renderText(f"Introduction"))
    sword = Item("Rusted sword", 2, 2, "weapon")
    health_potion = Item("Healing Potion", 1, 20, "potion")
    slime = Character(name="slime", health=50, gold=1)
    zombie = Character(name="slime", health=70, gold=3)

    # game statrt
    while True:
        lin_nbr = print_paragraph(list[i], lin_nbr)
        choice, row_nbr = choices(row_nbr,2)
        x = show_choices(choice)
        eval(x)
        i += 1
        if i == len(list):
            print("The End")
            sys.exit("see you on the next release")



def pargarph(line_nbr):
    ph = ""
    with open("story.txt", 'r') as file:
        for i, line in enumerate(file):
            if i < line_nbr:
                pass
            elif line.isspace():
                return ph, line_nbr+1
            else:
                ph += line
                line_nbr += 1
    return ph if ph else "The End", line_nbr


def print_paragraph(n, line_nbr):
    for _ in range(n):
        input("Tap any key")
        ph, line_nbr = pargarph(line_nbr)
        clear_terminal()
        print(ph)
    return line_nbr


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_panel(char):
    table = Table(title="Stats")
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Attribiut")
    table.add_row("Name:", char.name)
    table.add_row("Health:", str(char.health))
    table.add_row("Strength", str(char.strength))
    table.add_row("Mana:", str(char.mana))
    table.add_row("Gold", str(char.gold)+"🟡")
    console = Console()
    console.print(table)


def show_item(inventory):
    ch=""
    for i in range(len(inventory)):
        ch +=f"item {i+1} : {inventory[i]}\n"
    return ch


def choices(row_number, nbr_choices):
    choice_d = []
    with open("choice.csv", "r") as file:
        reader = csv.DictReader(file)
        for _ in range(row_number - 1):
            next(reader)
        for i in range(nbr_choices):
            try:
                choice = next(reader)
                choice_d.append(dict(choice))
            except StopIteration:
                break
    return choice_d, row_number + len(choice_d)


def show_choices(dic):
    for i in range(len(dic)):
        print(dic[i]['choice'])
    while True:
        choice = input("what is your choice: ").upper()
        for i in range(len(dic)):
            if dic[i]['choice'] == choice:
                return dic[i]['action']

        print("Invalid choice")


def fight(player, npc, inventory):
    while True:
        if not inventory:
            if npc.health <= 0:
                player.health = player.max_health
                player.gold = npc.gold
                return ("you won")
            elif player.health <= 0:
                sys.exit("Game Over")
            else:
                print(f"you dealt damage = {fight_round(npc,player)}")
                print(f"you took damage = {fight_round(player,npc)}")
                print(player.health)
                print(npc.health)

        else:
            try:
                while True:
                    choix = input("do you want to use item yes/no: ").upper()
                    if choix in ["YES", "NO"]:
                        break
            except ValueError:
                pass

            if choix == "NO":
                if npc.health <= 0:
                    player.health = player.max_health
                    player.gold = npc.gold
                    return ("you won")
                elif player.health <= 0:
                    sys.exit("Game Over")
                else:
                    print(f"you dealt damage = {fight_round(npc,player)}")
                    print(f"you took damage = {fight_round(player,npc)}")
                    print(player.health)
                    print(npc.health)
            else:
                print (show_item(inventory))
                i = 0
                try:
                    while True:
                        i = int(input("select item number: "))
                        if i and i in range(len(inventory)+1):
                            break
                except (ValueError, UnboundLocalError):
                    print("please select valid item number")
                    pass
                if i-1 in range(len(inventory)) and inventory[i-1].type == "weapon":
                    print(f"you dealt damage = {fight_round(npc,player,inventory[i-1],inventory)}")
                    print(f"you took damage = {fight_round(player,npc)}")
                    print(player.health)
                    print(npc.health)
                elif i-1 in range(len(inventory)) and inventory[i-1].type == "potion":
                    Item.use_potion(inventory[i-1], player, inventory)
                    print(f"you took damage = {fight_round(player,npc)}")
                elif npc.health <= 0:
                    player.health = player.max_health
                    player.gold = npc.gold
                    return ("you won")
                elif player.health <= 0:
                    sys.exit("Game Over")


def fight_round(*argv):
    if len(argv) == 2:
        x = random.randint(0, argv[1].strength)
        argv[0].health -= x
        return x
    else:
        x = (random.randint(0, argv[1].strength) + argv[2].attack)
        argv[0].health -= x
        Item.use_weapon(argv[2], argv[3])
        return x


if __name__ == "__main__":
    main()
