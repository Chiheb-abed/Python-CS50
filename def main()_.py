def main():
    while True:
        str = input ("saisir une chaine : ")
        if (len(str)>0 or len(str)<100) and (str[0].isalpha()):
            break
    print(len(str))
    str = str.lower()
    list=[]
    for word in str:
        list.append(word + " ")

    for lettre in list :
        print (lettre)
main()


