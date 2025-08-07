🔹 Aşama 1 – Cihaz Tespiti ve Takibi (ARP Watcher)

Ağ taraması yap (arp -a gibi)

MAC/IP eşleşmelerini logla

Yeni cihaz gelince veya IP/MAC çakışması olursa uyar

Basit CLI çıktısı yeterli

🔹 Aşama 2 – DNS Paket Dinleme (DNS Sniffer)

Scapy ile ağda dönen DNS sorgularını dinle

Hangi cihaz hangi domain'i sorguluyor, listele

Aynı domain’e farklı IP cevabı geliyorsa uyarı ver

🔹 Aşama 3 – Uyarı Sistemi & Loglama

Uyarıları terminalde göster

Ayrıca logları bir log.json veya alerts.txt dosyasına kaydet

(İleri seviye için: Telegram, mail veya basit web panel eklenebilir)    
