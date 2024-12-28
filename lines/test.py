def main():
    lvl= (get_level())
    print(lvl)

#test test
def get_level():
    while True:
        try:
            x= input("fraction : ")
            l=x.split('/')
            f=round((int(l[0])/int(l[1]))*100)
            if f>100 :
                continue
            elif f>98 :
                return "F"
            elif f<2 :
                return "E"
            else :
                return str(f)+"%"

        except (ValueError, ZeroDivisionError,IndexError):
            pass



main()
