
# Practica 2 1410767 


import requests
import pprint

def Organizations_Meraki(url,headers):
    r = requests.get(url, headers=headers)
    org_json = r.json()
    #pprint.pprint(org_json)
    org_list =[]
    for organization in org_json:
        org_list.append(organization['name'])
    return org_list
    

url = "https://api.meraki.com/api/v0/organizations"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}








