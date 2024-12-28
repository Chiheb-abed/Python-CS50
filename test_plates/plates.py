def main():
    plate = input ("plates : ")
    if is_valid(plate):
        print("valid")
    else:
        print("invalid")

def is_valid(s):
    l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    n = ['1','2','3','4','5','6','7','8','9']
    z = ['0','1','2','3','4','5','6','7','8','9']
    if ( len(s) >6) or (len(s) < 2 ):


        return False

    elif (s[0].upper() not in l) or (s[1].upper() not in l):


        return False
    elif (not s.isalnum()):

        return False
    for i in range (1,len(s)):
        if s[i].upper() in l :
            continue
        elif s[i] in n :
            break
        else:

            return False
    for i in range (i+1,len(s)):
        if s[i] not in z :

            return False
        else :
            continue
    return True
if __name__=="__main__":
    main()



