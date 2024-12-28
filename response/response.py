from validator_collection import validators, checkers, errors
def main():
    mail=input (f"What's your email address? ")
    print (validate(mail))



def validate(mail):
    if checkers.is_email(mail):
        return "Valid"
    else:
        return "Invalid"



if __name__=="__main__":
    main()
