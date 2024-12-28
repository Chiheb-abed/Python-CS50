def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num = ["0","1","2","3","4","5","6","7","8","9"]
    i = 0
    while i in range(len(s)):
        if  s[i] not in alphabet and s[i] not in num:
            
            return False
        elif s[i]  not in alphabet and s[i] in num and i < 1:

            return False
        else:
           if  check_num(i,s,num):

                return False
        i += 1
    return True

def check_num (x,txt,list):
    if txt[x] == 0:

        return False
    else:
        for x in range(len(txt)):
            if txt[x] in list:

                return False
        return True







main()