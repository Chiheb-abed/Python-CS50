from datetime import date , timedelta
import sys
import re
import inflect

p = inflect.engine()
class dates:
    def __init__(self,bdate):
        self.bdate= bdate

    def __str__(self):
        return (f"date: {self.bdate}")
    @classmethod
    def checkdate(cls, bdate):
        if re.match(r"\b\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2]\d|3[0-1])\b",bdate):
            return True
        else :
            return False

    @classmethod
    def getdate(cls):
        try:
            bdate = input ("Date of Birth: ")
            if dates.checkdate(bdate):
                return cls(bdate)
            else:
                sys.exit("Invalid Date")
        except :
            sys.exit("Invalid Date")

    @classmethod
    def convert(cls,bdate):
        today = date.today()
        return cls(today-date.fromisoformat(bdate))







def main():
    date = dates.getdate()
    sc = dates.convert(date.bdate)
    print (f"{(p.number_to_words(sc.bdate.days*24*60,andword="")).capitalize()} minutes")








if __name__ == "__main__":
    main()
