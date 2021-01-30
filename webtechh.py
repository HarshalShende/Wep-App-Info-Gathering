#!/usr/bin/env python3

import os,sys
from colorama import Fore, Back, Style
from termcolor import colored
try:
    import webtech
except:
    os.system("pip install webtech")

def webtech_result(domain):
    wt = webtech.WebTech(options={'json': True})

    report = wt.start_from_url(str(domain))
    tech = len(report['tech'])
    headers = len(report['headers'])
    print("***** Technologies *****")
    for i in range(0,tech):
        print(Fore.GREEN+str(report['tech'][i]['name'])+":"+str(report['tech'][i]['version']))
        print(Style.RESET_ALL)
    print("******************************************************************")
    print("***** Headers *****")
    for i in range(0,headers):
        print(Fore.BLUE+str(report['headers'][i]['name'])+":"+str(report['headers'][i]['value']))
        print(Style.RESET_ALL)
    

