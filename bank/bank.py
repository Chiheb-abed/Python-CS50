greet = input ("Greeting : ").strip()
if greet.lower().startswith("hello") :
    print ("$0")
elif greet[0].lower() == 'h':
    print("$20")
else:
    print("$100")