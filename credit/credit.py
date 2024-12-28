from cs50 import get_string , get_int

def main():
    card = get_string("Number: ")
    rev = card[::-1]
    if card[0]=="4" and calculate(rev) and len(card) in [13,16]:
        print("VISA")
    elif card[:2] in ["34","37"] and calculate(rev) and len(card)==15:
        print("AMEX")
    elif int(card[:2])>=51 and int(card[:2])<=55 and calculate(rev) and len(card)==16:
        print("MASTERCARD")
    else:
        print ("INVALID")


def calculate(card):
    i=0
    s=0
    ss=0
    for c in card:
        if (i%2)==1:
            ch= int(c)*2
            if ch>9:
                ch = str(ch)
                s+= int(ch[0]) + int(ch[1])
            else:
                s+= ch
        else:
            ss+=int(c)
        i += 1

    if (s+ss) % 10 == 0:
        return True
    else:
        return False

main()


