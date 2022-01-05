
# Practica 2 1410767 


import requests
import time
import pprint
import csv

def Organizations_Meraki(url,headers):
    r = requests.get(url, headers=headers)
    org_json = r.json()
    #pprint.pprint(org_json)
    org_list =[]
    for organization in org_json:
        org_list.append(organization['name'])
    return org_list
    
#Nueva funcion para realizar inventario
def Inventario(url, headers):
    r = requests.get(url, headers=headers)
    inventory_json = r.json()
    inventory_list=[]
    for item in inventory_json: 
        key = 'productType'
        if key in item:
            if item['productType'] == 'wireless' or item['productType'] == 'appliance':
                inventory_list.append(item)  
    
    keys = ['ProductType','Model','Name', 'MAC', 'LAN IP','Serial','Status' ]  
    
    with open("Inventory.csv",'w') as f:
        writer = csv.writer(f)
        writer.writerow(keys)
        f.close()

    for item in inventory_list:
        features = []
        features.append(item['productType'])
        features.append(item['model'])
        features.append(item['name'])
        features.append(item['mac'])
        features.append(item['lanIp'])
        features.append(item['serial'])
        features.append(item['configurationUpdatedAt'])
        with open("Inventory.csv",'a',newline = '' ) as f:
            writer = csv.writer(f)
            writer.writerow(features)
            f.close()
    

url = "https://api.meraki.com/api/v0/organizations"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}

url_devices = "https://api.meraki.com/api/v1/organizations/681155/devices"

start_time = time.time() - 300

while True:
    if time.time() - start_time >= 300:
        start_time = time.time()
        Inventario(url_devices,headers=headers)

    











