import sys,os
import whois

try:
    print(Fore.YELLOW+"Checking whois library")
    import whois
    print("Whois library is exist")
    print(Style.RESET_ALL)
    print(Fore.RED+"******************************************************************")
    print(Style.RESET_ALL)
except:
    print(Fore.YELLOW+"İnstalling whois library")
    os.system("pip3 install python-whois")
    print(Style.RESET_ALL)
    print(Fore.RED+"******************************************************************")
    print(Style.RESET_ALL)

def whois_result(dmn):
    w = whois.whois(str(dmn))
    domain_keys = []

    for i in w.keys():
        domain_keys.append(i)
    for i in domain_keys:
        print(str(i)+":"+str(w[i]))

if __name__ == '__main__':

    ans = input("Domain: ")
    whois_result(ans)
