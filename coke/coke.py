def main():
    money = [25,10,5]
    sum = ask_money(money)
    while sum < 50 :
        print ("Amount Due:", 50-sum)
        sum += ask_money(money)
    if sum == 50:
        print ("Change Owed: 0")
    else:
        print ("Change Owed:", sum-50)


def ask_money(mo):
    while True :
        amount = int(input(" Insert coin :  "))
        if amount in mo:
            return amount
        else :
            print ("Amount Due: 50")

main()