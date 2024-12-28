from cs50 import get_string

text = get_string ("text: ")
lettre =0
word=0
sent =0
for c in text:
    if c.isalpha():
        lettre+=1
    elif c == " ":
        word+=1
    elif c in [".","!","?"]:
        sent+=1
word+=1;
l= lettre / word * 100
s = sent / word * 100
index = 0.0588 * l - 0.296 * s - 15.8

if index < 0:
    print("Before Grade 1")
elif index > 16:
    print("Grade 16+")
else:
    print("Grade ",round(index))

