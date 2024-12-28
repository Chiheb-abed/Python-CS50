import sys
import requests
import json
def main():
    if len(sys.argv) != 2 :

        sys.exit("Missing command-line argument")
    elif isinstance(sys.argv[1] , float) :

        sys.exit("Command-line argument is not a number")
    else :
        try:
            ap = requests.get ("https://api.coindesk.com/v1/bpi/currentprice.json")
            list = ap.json()
            price =list["bpi"]["USD"]["rate_float"]
            
        except requests.RequestException :
            pass
    amount = float(float(sys.argv[1]) * float(price))
    print(f"${amount:,.4f}")












if __name__ == "__main__" :
    main()
