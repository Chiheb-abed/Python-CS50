import sys

def main():
    check_arg()
    print(count())




def check_arg():
    if len(sys.argv)<2 :
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>2 :
        sys.exit ("Too many command-line arguments")
    elif not (sys.argv[1].endswith(".py")):
        sys.exit ("Not a Python file")

def count():
    count = 0
    filename = sys.argv[1]
    try:
        with open (filename) as file:
            for line in file :
                if line.strip().startswith("#"):
                    pass
                elif line.isspace() == True:
                    pass
                else:
                    count += 1
    except FileNotFoundError:
        sys.exit("File does not exist")
    return count




if __name__=="__main__":
    main()
