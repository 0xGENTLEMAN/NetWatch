**"This project is a work in progress, and I'm still improving it."**
NETwatch 

**NETwatch** is a simple Python tool that monitors your local network using ARP scans.  
It detects:
- 🆕 **New devices** joining the network  
- ❌ **Devices leaving** the network  
- 🔄 **MAC address changes** (possible spoofing)  
- 🌐 **IP address changes** for the same MAC  

---

Features
- Automatic ARP scanning with [`scapy`](https://scapy.net/)
- Saves device list to `devices.json`
- Real-time detection of network changes
- Easy to customize network interface & IP range

---

Requirements
```bash
pip install scapy
```
