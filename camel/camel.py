def main ():
    name = input ("camelCase : ")
    if name.islower():
        print(name)
    else:
        snake_name(name)


def snake_name (snake):
    ch = ""
    for i in range(len(snake)):
        if snake[i].islower():
            ch += snake[i]
        elif i == 0:
            ch += snake[i].lower()
        else:
            ch+= "_" + snake[i].lower()
    print(ch)
main()

