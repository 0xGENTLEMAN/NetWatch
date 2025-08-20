from scapy.all import ARP, Ether, srp
import json
import time

print("NETwatch:")

def arp_scan():
    interface = "wlp2s0"        # Tarama yapılacak ağ arayüzü
    address = "10.156.101.0/24" # Tarama yapılacak IP aralığı

    print("INTERFACE:", interface, "ADDRESS:", address)

    arp_req = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=address)
    answered, unanswered = srp(arp_req, timeout=2, verbose=0)

    ip_mac_dict = {}
    for sent, received in answered:
        ip_mac_dict[received.psrc] = received.hwsrc

    return ip_mac_dict


# İlk tarama
ip_mac_dict = arp_scan()

# JSON dosyasına yaz
with open("devices.json", "w") as f:
    json.dump(ip_mac_dict, f, indent=4)

print("Cihaz listesi kaydedildi:", ip_mac_dict)


# Sürekli kontrol döngüsü
while True:
    # Eski taramayı JSON'dan oku
    with open("devices.json", "r") as f:
        first_scan = json.load(f)

    # Yeni tarama yap
    new_scan = arp_scan()

    # Yeni cihazlar
    new_devices = set(new_scan.keys()) - set(first_scan.keys())
    for ip in new_devices:
        print(f"Yeni cihaz bulundu: {ip} >> {new_scan[ip]}")

    # Kaybolan cihazlar
    old_devices = set(first_scan.keys()) - set(new_scan.keys())
    for ip in old_devices:
        print(f"Cihaz ayrıldı: {ip} -> {first_scan[ip]}")

    # Aynı IP’de MAC değişmişse
    for ip in set(new_scan.keys()).intersection(first_scan.keys()):
        if new_scan[ip] != first_scan[ip]:
            print(f"{ip} MAC DEĞİŞMİŞ: {first_scan[ip]} -> {new_scan[ip]}")

    # Aynı MAC farklı IP almışsa
    first_scan_mac_to_ip = {mac: ip for ip, mac in first_scan.items()}
    new_scan_mac_to_ip   = {mac: ip for ip, mac in new_scan.items()}

    for mac in set(new_scan_mac_to_ip.keys()).intersection(first_scan_mac_to_ip.keys()):
        if new_scan_mac_to_ip[mac] != first_scan_mac_to_ip[mac]:
            print(f"{mac} IP DEĞİŞMİŞ: {first_scan_mac_to_ip[mac]} -> {new_scan_mac_to_ip[mac]}")

    # JSON dosyasını güncelle (bir sonraki döngü için)
    with open("devices.json", "w") as f:
        json.dump(new_scan, f, indent=4)

    # 20 saniye bekle
    time.sleep(20)




