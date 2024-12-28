import random

def main():
    n= get_level()
    scr = rounds(n)
    print ("Score: ",scr)



def get_level ():
    while True:
        try:
            n= int(input ("Level: "))
            if n in [1,2,3] :
                break
        except:
            pass
    return n
def generate_integer (n):
    if n == 1 :
        return random.randint(0,9)
    elif n == 2 :
        return random.randint(10,99)
    else :
        return random.randint(100,999)

def game (x,y):
    j=1
    while j < 4 :
        try:
            r=int(input(f"{x} + {y} = "))
            if r == x+y :
                return True
            else:
                j+=1
                print("EEE")
        except:
            j+=1
            print("EEE")

    print (f"{x} + {y} = {x+y}")
    return False

def rounds (n):
    round = 0
    s=0
    while round < 10:
        x=generate_integer(n)
        y=generate_integer(n)
        res = game (x,y)
        if res == True :
            s+=1
        round+=1
    return s





if __name__ == "__main__" :
    main()
