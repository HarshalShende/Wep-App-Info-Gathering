import sys,os,json
import requests
from colorama import Fore, Back, Style
from termcolor import colored

def dns_resolve(dmn):
    try:
        r2 = requests.get("https://api.shodan.io/dns/resolve?hostnames="+str(dmn)+"&key=API_KEY")
        response = json.loads(r2.text)
        for i in response:
            print(Fore.GREEN+str(i)+" ---> "+str(response[i]))
            print(Style.RESET_ALL)
    except:
        print(Fore.RED+"Not Found")
        print(Style.RESET_ALL)

def dns_reverse(ip):
    try:
        r3 = requests.get("https://api.shodan.io/dns/reverse?ips="+str(ip)+"&key=API_KEY")
        response=json.loads(r3.text)
        for i in response:
            print(Fore.GREEN+str(i)+" ---> "+str(response[i]))
            print(Style.RESET_ALL)
    except:
        print(Fore.RED+"Not Found")
        print(Style.RESET_ALL)
