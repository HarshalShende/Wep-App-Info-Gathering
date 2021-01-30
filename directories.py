import os,sys
from colorama import Fore, Back, Style
from termcolor import colored

try:
    print(Fore.YELLOW+"Checking Dirb Tool")
    print("\n")
    if os.path.isfile('/usr/bin/dirb'):
        print('[+] Dirb is Exist')
    print(Style.RESET_ALL)
    print(Fore.RED+"******************************************************************")
    print(Style.RESET_ALL)
except:
    print(Fore.YELLOW+"İnstalling Dirb Tool")
    os.system("apt-get install dirb")
    print(Style.RESET_ALL)
    print(Fore.RED+"******************************************************************")
    print(Style.RESET_ALL)

def fast_listing(dmn):

    os.system("dirb "+str(dmn)+" dir.txt -X .txt,.log,.conf,.config,.cfg,.db,.sql,.bak,.old,.xml -S > fast_listing.txt")
    file = open("fast_listing.txt","r")
    for i in file.readlines():
        if "CODE:200" in str(i):
            print(Fore.GREEN+str(i))
            print(Style.RESET_ALL)

def normal_listing(dmn):

    print(Fore.GREEN)
    os.system("dirb "+str(dmn)+" -S")
    print(Style.RESET_ALL)

