def main():
    glist={}
    while True:
        try:
            item = input().upper()
            if item in glist :
                glist[item] += 1
            else:
                glist[item] = 1
        except EOFError:
            break
    sglist = dict(sorted(glist.items()))
    for key in sglist:
        print (sglist[key],key)





main()
