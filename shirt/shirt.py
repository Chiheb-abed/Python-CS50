import sys
from PIL import Image , ImageOps







def main():
    check_arg()
    images()



def check_arg():
    if len(sys.argv)<3 :
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>3 :
        sys.exit ("Too many command-line arguments")
    elif sys.argv[1][sys.argv[1].find("."):].lower() != sys.argv[2][sys.argv[2].find("."):].lower():
        sys.exit ("Input and output have different extensions")
    elif sys.argv[1][sys.argv[1].find("."):].lower() not in [".jpg" , ".jpeg" , "png"] or sys.argv[2][sys.argv[2].find("."):].lower() not in [".jpg" , ".jpeg" , "png"]:
        sys.exit ("Invalid input")


def images():
    try:
        img = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
        w = shirt.width
        h = shirt.height
        img = ImageOps.fit(img,(w,h))
        img.paste(shirt,shirt)
        img.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")




if __name__=="__main__":
    main()
