def main():
    msg = input ("write a message :  ")
    print (shorten (msg))


def shorten (txt):
    new_msg = ""
    vowls = ["a","e","i","o","u"]
    for lettre in txt:
        if lettre.lower() not in vowls:
            new_msg += lettre
    return new_msg

if __name__ == "__main__":
    main()
