import inflect
p = inflect.engine()
list = []
while True:
    try:
        name =input ("name: ")
        list.append(name)

    except EOFError:
        print()
        break
mylist=p.join(list)
print ("Adieu, adieu, to" , mylist )


