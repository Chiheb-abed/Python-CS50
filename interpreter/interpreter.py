e = input ("Expression : ").strip()
x , y , z = e.split(" ")
match y :
    case "+" :
        print (float(int(x) + int(z)))
    case "-" :
        print (float(int(x) - int(z)))
    case "*" :
        print (float(int(x) * int(z)))
    case _ :
        print (float (round (int(x) / int(z) , 1)))
