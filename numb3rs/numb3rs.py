import re



def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ips =[]
    if ipv :=re.search (r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$",ip):
            ips = (int(ipv.group(1)), int(ipv.group(2)) , int(ipv.group(3)) , int(ipv.group(4)))
            for ipp in ips :
                 if ipp<0 or ipp > 255 :
                    return False
                 else :
                    pass
            return True
    else:
        return False




if __name__ == "__main__":
    main()
