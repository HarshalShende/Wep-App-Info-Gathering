#!/usr/bin/env python3
import os,sys
from colorama import Fore, Back, Style
from termcolor import colored

try:
    print(Fore.YELLOW+"Checking Wafw00f Tool")
    print("\n")
    if os.path.isfile('/usr/bin/wafw00f'):
        print('[+] Wafw00f is Exist')
    print(Style.RESET_ALL)
    print(Fore.RED+"******************************************************************")
    print(Style.RESET_ALL)
except:
    print(Fore.YELLOW+"İnstalling Wafw00f Tool")
    os.system("apt-get install wafw00f")
    print(Style.RESET_ALL)
    print(Fore.RED+"******************************************************************")
    print(Style.RESET_ALL)
try:
    print(Fore.YELLOW+"Checking Lbd Tool")
    print("\n")
    if os.path.isfile('/usr/bin/lbd'):
        print('[+] Lbd is Exist')
    print(Style.RESET_ALL)
    print(Fore.RED+"******************************************************************")
    print(Style.RESET_ALL)
except:
    print(Fore.YELLOW+"İnstalling Lbd Tool")
    os.system("apt-get install lbd")
    print(Style.RESET_ALL)
    print(Fore.RED+"******************************************************************")
    print(Style.RESET_ALL)

def wafandlbd_show(domain):

    print("Web Application Firewall Detection")
    result = os.system('wafw00f '+str(domain)+' |grep "behind"')
    if str(result) == "256":
       print(Fore.RED+"WAF NOT FOUND")
    else:
       print(Fore.GREEN+str(result))
    os.system('sleep 2\n')
    print(Style.RESET_ALL)
    print("****************************************************************")
    print("Load Balancer Detection")
    os.system('lbd '+str(domain))
    print("****************************************************************")
