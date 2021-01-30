import os,sys
from colorama import Fore, Back, Style
from termcolor import colored

try:
    print(Fore.YELLOW+"Checking Nmap Tool")
    print("\n")
    if os.path.isfile('/usr/bin/nmap'):
        print('[+] Nmap is Exist')
    print(Style.RESET_ALL)
    print(Fore.RED+"******************************************************************")
    print(Style.RESET_ALL)
except:
    print(Fore.YELLOW+"İnstalling Nmap Tool")
    os.system("apt-get install nmap")
    print(Style.RESET_ALL)
    print(Fore.RED+"******************************************************************")
    print(Style.RESET_ALL)

def nmap_result(answer):

    os.system("nmap -sS -sV -p80,81,443,8081 -T4 "+str(answer)+" --open > nmap_result.txt")
    result1 = os.system("cat nmap_result.txt|grep 80/tcp")
    result2 = os.system("cat nmap_result.txt|grep 81/tcp")
    result3 = os.system("cat nmap_result.txt|grep 443/tcp")
    result4 = os.system("cat nmap_result.txt|grep 8081/tcp")
    
    if "open" in str(result1):
        print(Fore.GREEN+str(result1))
        print(Style.RESET_ALL)
    elif "open" in str(result2):
        print(Fore.GREEN+str(result2))
        print(Style.RESET_ALL)
    elif "open" in str(result3):
        print(Fore.GREEN+str(result3))
        print(Style.RESET_ALL)
    elif "open" in str(result4):
        print(Fore.GREEN+str(result4))
        print(Style.RESET_ALL) 

