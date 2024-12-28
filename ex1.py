list =[]
while True :
    n = int (input ("saisir n  : "))
    if n > 0 :
        break
i=0
while i<n :
    nbr = int (input ("saisir un nbr positive = "))
    if nbr > 0 :
        list.append(nbr)
        i=i+1
    else:
        continue
j=0
for number in list :
    if number == 6 :
        j+=1
print("number of occurance de 6 = " , j)
list.sort()
print("list trier = ",list)
nlist = list.copy()
print ("new list = ", nlist)
print ("min = " , nlist[0])
print ("max = " , nlist [n-1])
p=1
for nb in nlist :
    if (nb > 1) and (nb <= 10 ):
        p = p*nb
print ("le produit est = " , p)
while True :
    x = int (input ("saisir un nbr positive "))
    if x > 0 :
        break
for k in range(n) :
    if nlist[k] == x:
        print ("postion de " , x ,"= " , k)
nlist.remove(x)
print("list sans x = " , nlist )
for nim in range(n) :
    nlist[nim] += 4
print ("list avec 4" , nlist)





.