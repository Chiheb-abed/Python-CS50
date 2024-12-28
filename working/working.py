import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
        if matches := re.search(r"^(\d+(:\d+)?) (AM|PM) to (\d+(:\d+)?) (AM|PM)$" , s,re.IGNORECASE):
             l= matches.group(1).split(":")
             d = matches.group(4).split(":")
             l=check_list(l)
             d=check_list(d)
             l = turn (l,matches.group(3))
             d= turn (d,matches.group(6))

        else:
            raise ValueError
        return l[0]+":"+l[1]+" to "+d[0]+":"+d[1]

def check_list(l):
     if int (l[0]) in range(1,13) and len(l) == 1:
            l.append("00")
            return l
     elif int (l[0]) in range(1,13) and int(l[1])  in range (0,60):
           return l
     else:
            raise ValueError


def turn(l,x):
      if x == "PM" and l[0] != "12":
            l[0] = str (int(l[0])+12)
      elif x == "AM" and l[0] == "12" :
            l[0] = "00"
      elif int (l[0]) < 10:
            l[0] = "0" + l[0]

      return l






if __name__ == "__main__":
    main()
