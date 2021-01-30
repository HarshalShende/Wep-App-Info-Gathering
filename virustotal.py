import sys,os
import requests,json
from colorama import Fore, Back, Style
from termcolor import colored

def domain(dmn):

    header = {"x-apikey":"API_KEY"}
    r = requests.get("https://www.virustotal.com/api/v3/domains/"+str(dmn),headers=header)
    results = r.json()
    print(Fore.GREEN+"Harmless: "+str(results['data']['attributes']['last_analysis_stats']['harmless']))
    print(Style.RESET_ALL)
    print(Fore.RED+"Malicious: "+str(results['data']['attributes']['last_analysis_stats']['malicious']))
    print(Style.RESET_ALL)
    print(Fore.YELLOW+"Suspicious: "+str(results['data']['attributes']['last_analysis_stats']['suspicious']))
    print(Style.RESET_ALL)
    print("******************************************************************")
    print("Engine name ---- Results")
    print("------------------------")
    for i in results['data']['attributes']['last_analysis_results'].values():
        if i['result'] == "clean":
            print(Fore.GREEN+i['engine_name']+" -- "+i['result'])
            print(Style.RESET_ALL)
        else:
            print(Fore.RED+i['engine_name']+" -- "+i['result'])
