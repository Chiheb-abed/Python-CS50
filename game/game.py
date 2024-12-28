def main():
   import random
   n= postive_int("level = ")
   randon = random.randint(1,n)
   while True :
        guess = postive_int ("Guess: ")
        if guess < randon :
            print ("Too small!")
            continue
        elif guess > randon :
            print ("Too large!")
            continue
        else :
            print ("Just right!")
            break



def postive_int(prompt):
      while True:
        try:
            n = int (input(prompt))
            if n < 1 or n > 101:
                continue
            else :
                return n
        except ValueError:
            pass




if __name__=="__main__":
    main()
