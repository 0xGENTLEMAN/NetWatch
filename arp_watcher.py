import scapy
import sys    
import subprocess
import json

print("NETwatch:")

interface = input("Lütfen interface giriniz:")
adddress = input("Lütfen bir aralık belirtiniz:")  #10.156.101.7

print("İNTERFACE:",interface,"ADDRESS:",adddress)

scan = subprocess.run(
    ["arp-scan",interface,adddress]
    ,capture_output=True
    ,text=True)

print("Normal Çıktı \n",scan.stdout)
print("Hatalı Çıktı \n",scan.stderr)

ip_mac_dict = {}

for line in scan.stdout.splitlines():
    parts = line.split()
    if len(parts) >= 2 and parts[0].count(".") == 3:
        ip = parts[0]
        mac = parts[1]
        ip_mac_dict[ip] = mac

with open("devices.json", "w") as f:
    json.dump(ip_mac_dict, f, indent=4)

print("Cihaz listesi kaydedildi:", ip_mac_dict)
