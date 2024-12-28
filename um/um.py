import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    if l := re.findall(r"\bum\b",s,re.IGNORECASE):
        return len(l)
    else:
        return 0






if __name__ == "__main__":
    main()
