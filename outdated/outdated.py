months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    try :
        date = input ("Date:  ").title()

        if date[0].isalpha() and date.find(" ") != -1 and date.find(", ") != -1 :
            month,day,year = date.split(" ")
            monthnum =int( months.index(month) +1)
            day = int (day.replace("," , ""))
            if day < 1 or day > 31 :
                continue;
            else :
                year = int (year)
                print (f"{year}-{monthnum:02}-{day:02}")


            break;

        elif date.find ("/") != -1 and date.find("/",3):

            month,day,year = date.split("/")
            month = int(month)
            day = int(day)
            year = int (year)
            if day < 1 or day > 31 or month < 0 or month >12 :
                continue;
            else :

                print (f"{year}-{month:02}-{day:02}")
            break;
    except (ValueError) :
        pass


