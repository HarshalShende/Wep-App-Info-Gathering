import os,sys
import requests,json
from colorama import Fore, Back, Style
from termcolor import colored


def subdomains(s):
    url = "https://api.securitytrails.com/v1/domain/"+str(s)+"/subdomains"
    querystring = {"children_only": "false"}
    headers = {
        "Accept": "application/json",
        "APIKEY": "API_KEY"
    }
    r = requests.request("GET", url, headers=headers, params=querystring)
    response = json.loads(r.text)
    total = len(response['subdomains'])
    sıra = 1
    file_name = s.split(".")[0]
    f = open(str(file_name)+".txt","a+")
    print("***** SUBDOMAINS ("+str(total)+") *****")
    for i in response['subdomains']:
        #print(str(sıra)+")"+str(i)+"."+str(s))
        f.writelines(str(sıra)+")"+str(i)+"."+str(s)+"\n")
        sıra = sıra + 1
    print(Fore.GREEN+str(sıra)+" subdomains detected")
    print(Style.RESET_ALL)
    f.close()
