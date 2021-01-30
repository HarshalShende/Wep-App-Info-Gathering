import sys,os
import requests
from colorama import Fore, Back, Style
from termcolor import colored

def http_header_check(dmn):
    r = requests.options(str(dmn))
    try:
        print(Fore.GREEN+"Allowed Headers: "+str(r.headers['Allow']))
        print(Style.RESET_ALL)
    except:
        print(Fore.RED+"It doesn't has any allowed header")
        print(Style.RESET_ALL)

def httponly_and_secure(dmn):
    r = requests.get(str(dmn))

    try:
        if "Secure" in r.headers['Set-Cookie']:
            print(Fore.GREEN+"Secure header set")
            print(Style.RESET_ALL)
        elif "secure" in r.headers['Set-Cookie']:
            print(Fore.GREEN+"Secure header set")
            print(Style.RESET_ALL)
    except:
        print(Fore.RED+"Secure header not exist")
        print(Style.RESET_ALL)

    try:
        if "HttpOnly" in r.headers['Set-Cookie']:
            print(Fore.GREEN+"HttpOnly header set")
            print(Style.RESET_ALL)
        elif "httponly" in r.headers['Set-Cookie']:
            print(Fore.GREEN+"HttpOnly header set")
            print(Style.RESET_ALL)
    except:
        print(Fore.RED+"HttpOnly header not exist")
        print(Style.RESET_ALL)


