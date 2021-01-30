#!/usr/bin/env python3

import os,sys
import requests
from colorama import Fore, Back, Style
from termcolor import colored

def txt(domain):

    r1 = requests.get("http://www."+str(domain)+"/robots.txt")
    r2 = requests.get("https://www."+str(domain)+"/robots.txt")
    
    if r1.status_code == 200 and r2.status_code == 200:
        file = open("robots.txt","w")
        file.write(r2.text)
        print(Fore.GREEN+"Robots.txt created")
        print(Style.RESET_ALL)
    elif r1.status_code == 200:
        file = open("robots.txt","w")
        file.write(r1.text)
        print(Fore.GREEN+"Robots.txt created")
        print(Style.RESET_ALL)
    else:
        print(Fore.RED+"Robots.txt not exist")
        print(Style.RESET_ALL)

def sitemap_xml(domain):

    r1 = requests.get("http://www."+str(domain)+"/sitemap.xml")
    r2 = requests.get("https://www."+str(domain)+"/sitemap.xml")

    if r1.status_code == 200 and r2.status_code == 200:
        file = open("sitemap.xml","w")
        file.write(r2.text)
        print(Fore.GREEN+"Sitemap.xml created")
        print(Style.RESET_ALL)
    elif r1.status_code == 200:
        file = open("sitemap.xml","w")
        file.write(r1.text)
        print(Fore.GREEN+"Sitemap.xml created")
        print(Style.RESET_ALL)
    else:
        print(Fore.RED+"Sitemap.xml not exist")
        print(Style.RESET_ALL)

def crossdomain_xml(domain):

    r1 = requests.get("http://www."+str(domain)+"/crossdomain.xml")
    r2 = requests.get("https://www."+str(domain)+"/crossdomain.xml")

    if r1.status_code == 200 and r2.status_code == 200:
        file = open("crossdomain.xml","w")
        file.write(r2.text)
        print(Fore.GREEN+"Crossdomain.xml created")
        print(Style.RESET_ALL)
    elif r1.status_code == 200:
        file = open("crossdomain.xml","w")
        file.write(r1.text)
        print(Fore.GREEN+"Crossdomain.xml created")
        print(Style.RESET_ALL)
    else:
        print(Fore.RED+"Crossdomain.xml not exist")
        print(Style.RESET_ALL)

