import sys
import csv
from tabulate import tabulate

def main():
    check_arg()
    menu()




def check_arg():
    if len(sys.argv)<2 :
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>2 :
        sys.exit ("Too many command-line arguments")
    elif not (sys.argv[1].endswith(".csv")):
        sys.exit ("Not a CSV file")

def menu():
    filename = sys.argv[1]
    try:
        with open (filename) as file:
            reader = csv.DictReader(file)
            print(tabulate(reader,headers="keys",tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__=="__main__":
    main()

