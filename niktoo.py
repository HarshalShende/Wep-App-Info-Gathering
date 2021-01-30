import os,sys

try:
    print(Fore.YELLOW+"Checking Nikto Tool")
    print("\n")
    if os.path.isfile('/usr/bin/nikto'):
        print('[+] Nikto is Exist')
    print(Style.RESET_ALL)
    print(Fore.RED+"******************************************************************")
    print(Style.RESET_ALL)
except:
    print(Fore.YELLOW+"İnstalling Nikto Tool")
    os.system("apt-get install nikto")
    print(Style.RESET_ALL)
    print(Fore.RED+"******************************************************************")
    print(Style.RESET_ALL)

def nikto_result(dmn,con):

    if str(con) == "https":
        os.system("nikto -h https://"+str(dmn))
    else:
        os.system("nikto -h http://"+str(dmn))

