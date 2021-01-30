#!/usr/bin/env python3
import sys,requests,os
import banner,wafandlbd,xmlandtxt,virustotal,nmapp,niktoo,whoo,webtechh,subdomains,directories,securee,dnssenum
try:
    from colorama import Fore, Back, Style
except:
    os.system("pip3 install colorama")
try:
    from termcolor import colored
except:
    os.system("pip3 install termcolor")

banner.banner_echo()
print(Fore.RED+"******************************************************************")
print(Style.RESET_ALL)
try:
    print(Fore.YELLOW+"Checking json library")
    import json
    print("Json library is exist")
    print(Style.RESET_ALL)
    print(Fore.RED+"******************************************************************")
    print(Style.RESET_ALL)
except:
    print(Fore.YELLOW+"İnstalling json library")
    os.system("pip3 install json")
    print(Style.RESET_ALL)
    print(Fore.RED+"******************************************************************")
    print(Style.RESET_ALL)
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
try:
    print(Fore.YELLOW+"Checking Webtech library")
    import webtech
    print("Webtech library is exist")
    print(Style.RESET_ALL)
    print(Fore.RED+"******************************************************************")
    print(Style.RESET_ALL)
except:
    print(Fore.YELLOW+"İnstalling Webtech library")
    os.system("pip install webtech")
    print(Style.RESET_ALL)
    print(Fore.RED+"******************************************************************")
    print(Style.RESET_ALL)
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
os.system('sleep 5')
os.system('clear')
banner.banner_echo()
print(Fore.RED+"******************************************************************")
print(Style.RESET_ALL)
os.system('uname -an|cut -d " " -f 1-3')
try:
    r = requests.get("http://ifconfig.me/ip")
    print("My IP Adresses: "+str(r.text))
except:
    print("Doesn't Have Internet Connection")
print(Fore.RED+"******************************************************************")
print(Style.RESET_ALL)
def menu():

    print("1)Directories                             6)Weptech       11)Dns")
    print("2)Subdomains                              7)Whois         12)Quit")
    print("3)HTTP Option / Cookie                    8)Nikto")
    print("4)Virustotal                              9)Port Scaning")
    print("5)Sitemap.xml,Robots.txt,Crossdomain.xml  10)Wafw00f/Lbd")

if __name__ == '__main__':
    while True:
        menu()
        print("\n")
        ans = input("Select:")
        if ans == "1":
           print(Fore.RED+"******************************************************************")
           print(Style.RESET_ALL)
           print(Fore.BLUE+"***** Directories *****")
           print(Style.RESET_ALL)
           ans2 = input("1)Fast Listing\n2)Normal Listing: ")
           ans3 = input("Full Domain(https://www.google.com): ")
           print("\n")
           if ans2 == "1":
               directories.fast_listing(ans3)
           else:
               directories.normal_listing(ans3)
           print(Fore.RED+"******************************************************************")
           print(Style.RESET_ALL)
        elif ans == "2":
           print(Fore.RED+"******************************************************************")
           print(Style.RESET_ALL)
           ans2 = input("Domain(google.com): ")
           print("\n")
           subdomains.subdomains(ans2)
           print(Fore.RED+"******************************************************************")
           print(Style.RESET_ALL)
        elif ans == "3":
           print(Fore.RED+"******************************************************************")
           print(Style.RESET_ALL)
           print(Fore.BLUE+"***** HTTP OPTION / COOKIE *****")
           print(Style.RESET_ALL)
           ans2 = input("Domain(https://www.google.com): ")
           print("\n")
           securee.http_header_check(ans2)
           securee.httponly_and_secure(ans2)
           print(Fore.RED+"******************************************************************")
           print(Style.RESET_ALL)
        elif ans == "4":
           print("***** Virustotal Results *****")
           ans2 = input("Domain(google.com): ")
           print("\n")
           virustotal.domain(ans2)
           print(Fore.RED+"******************************************************************")
           print(Style.RESET_ALL)
        elif ans == "5":
           ans2 = input("Domain(google.com): ")
           print("\n")
           print(Fore.BLUE+"***** Robots.txt *****")
           print(Style.RESET_ALL)
           xmlandtxt.txt(ans2)
           print(Fore.RED+"******************************************************************")
           print(Style.RESET_ALL)
           print(Fore.BLUE+"***** Sitemap.xml *****")
           print(Style.RESET_ALL)
           xmlandtxt.sitemap_xml(ans2)
           print(Fore.RED+"******************************************************************")
           print(Style.RESET_ALL)
           print(Fore.BLUE+"***** Crossdomain.xml *****")
           print(Style.RESET_ALL)
           xmlandtxt.crossdomain_xml(ans2)
           print(Fore.RED+"******************************************************************")
           print(Style.RESET_ALL)
        elif ans == "6":
           print(Fore.RED+"******************************************************************")
           print(Style.RESET_ALL)
           print(Fore.BLUE+"***** Webtech Results *****")
           print(Style.RESET_ALL)
           ans2 = input("Domain(https://www.google.com): ")
           print("\n")
           webtechh.webtech_result(ans2)
           print(Fore.RED+"******************************************************************")
           print(Style.RESET_ALL)
        elif ans == "7":
           print("******************************************************************")
           print(Fore.BLUE+"***** Whois Results *****")
           print(Style.RESET_ALL)
           ans2 = input("Domain(google.com): ")
           print("\n")
           whoo.whois_result(ans2)
           print(Fore.RED+"******************************************************************")
           print(Style.RESET_ALL)
        elif ans == "8":
           print(Fore.RED+"******************************************************************")
           print(Style.RESET_ALL)
           print(Fore.BLUE+"***** Nikto Scanning *****")
           print(Style.RESET_ALL)
           ans2 = input("Domain(google.com): ")
           ans3 = input("Http/Https: ")
           print("\n")
           print(Fore.RED+"**************************")
           print(Style.RESET_ALL)
           niktoo.nikto_result(ans2,ans3)
           print(Fore.RED+"******************************************************************")
           print(Style.RESET_ALL)
        elif ans == "9":
           print(Fore.RED+"******************************************************************")
           print(Style.RESET_ALL)
           print(Fore.BLUE+"***** Port Scanning *****")
           print(Style.RESET_ALL)
           ans2 = input("Domain(google.com): ")
           print("\n")
           nmapp.nmap_result(ans2)
           print(Fore.RED+"******************************************************************")
           print(Style.RESET_ALL)
        elif ans == "10":
           ans2 = input("Domain(google.com): ")
           print("\n")
           wafandlbd.wafandlbd_show(ans2)
        elif ans == "11":
           print(Fore.RED+"******************************************************************")
           print(Style.RESET_ALL)
           ans2 = input("1)Dns resolve & 2)Dns reverse: ")
           print("\n")
           if ans2 == "1":
               ans3 = input("Domain(google.com,ghroot.com): ")
               dnssenum.dns_resolve(ans3)
           elif ans2 == "2":
               ans3 = input("Ip adresses(1.2.3.4,5.6.7.8): ")
               dnssenum.dns_reverse(ans3)
           print(Fore.RED+"******************************************************************")
           print(Style.RESET_ALL)
        elif ans == "12":
           print(Fore.YELLOW+"Quitting... Bye Bye")
           print(Style.RESET_ALL)
           sys.exit(0)
