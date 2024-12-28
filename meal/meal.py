def main():
    time = input ("what time is it ? ")
    meal = convert (time)

    if 7 <= meal <= 8 :
        print ("breakfast time ")
    elif 12 <= meal <= 13 :
        print ("lunch time ")
    elif 18 <= meal <= 19 :
        print ("dinner time ")



def convert (time):
    temp , jikan = time.split(":")
    return float(temp) + round(float(jikan)/60 , 2)




if __name__ == "__main__":
    main()
