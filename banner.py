#!/usr/bin/env python3
import os,sys
try:
    import pyfiglet
except:
    os.system("pip3 install pyfiglet")
try:
    from colorama import Fore, Back, Style
except:
    os.system("pip3 install colorama")
try:
    from termcolor import colored
except:
    os.system("pip3 install termcolor")

def banner_echo():

	banner = pyfiglet.figlet_format('GHROOT WEB APP PENTESTING',width=1000)

	print(Fore.BLUE+banner)
	print(Style.RESET_ALL)
