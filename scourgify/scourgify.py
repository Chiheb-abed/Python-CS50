import sys
import csv

def main():
    check_arg()
    order()





def check_arg():
    if len(sys.argv)<3 :
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>3 :
        sys.exit ("Too many command-line arguments")

def order ():
    filename = sys.argv[1]
    output=sys.argv[2]
    students=[]
    try:
        with open (filename) as file:
            reader = csv.DictReader(file)
            for row in reader :
                last,name=row["name"].split(",")
                students.append({"last name":last ,"name":name.strip() , "house":row['house']})
        with open(output, 'w' , newline='') as csvfile:
            fieldnames = ['first', 'last' , 'house']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in students :
                writer.writerow( {"first":row['name'],"last":row['last name'], "house":row['house']})
    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")








if __name__=="__main__":
    main()
