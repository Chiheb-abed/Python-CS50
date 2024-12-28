import sys
def main():
     fraction = input ("fraction: ")
     x = convert(fraction)
     f = gauge(x)
     print(f)


def convert(fraction):
    while True :
        try:
            l=fraction.split('/')
            if round((int(l[0])/int(l[1]))*100) <= 100 :
                return round((int(l[0])/int(l[1]))*100)
            else :
                fraction = input ("fraction: ")
                pass
        except (ValueError, ZeroDivisionError,IndexError) :
            raise


def gauge(percentage):
    if percentage>=99 :
        z="F"
    elif percentage<=1 :
        z="E"
    else :
        z = (str(percentage)+"%")
    return z


if __name__=="__main__":
    main()
