def main():
    msg = input ("write a message :  ")
    vowl (msg)

def shorten (txt):
    new_msg = ""
    vowls = ["a","e","i","o","u"]
    for lettre in txt:
        if lettre.lower() not in vowls:
            new_msg += lettre
    print (new_msg)

main()
