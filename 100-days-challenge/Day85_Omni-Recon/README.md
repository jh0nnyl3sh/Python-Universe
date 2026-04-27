# 👁️‍🗨️ Omni-Recon: Digital Footprint & OSINT Scanner

> **⚠️ WARNING:** > This tool is developed for educational purposes and authorized Red Team operations only. 
> The developer assumes no liability and is not responsible for any misuse or damage caused by this program.

**Omni-Recon** is an advanced, multithreaded Open Source Intelligence (OSINT) tool written in Python. It is designed to automate the reconnaissance phase of a penetration test by aggregating data from various public APIs, telecom databases, and data breach repositories.

### ⚔️ The Arsenal (Features)

* 🌐 **IP & Geo-Location Recon:** Resolves IP addresses to exact geographical coordinates, ISPs, and Timezones.
* 👤 **Digital Footprint (Username) Scanner:** Utilizes multithreading to rapidly scan 10+ popular social media and developer platforms (GitHub, Twitter, Reddit, etc.) for a specific username.
* 📱 **Advanced Telecom Recon:** Parses international phone numbers to extract Carrier, Line Type (Mobile/Fixed), Region, and Timezone metadata.
* 📧 **Email Breach & Reputation Scan:** Checks target emails against known data breaches and extracts linked social media profiles.
    * *Evasion Tactics:* Features a built-in proxy rotation system scraping live anonymous proxies from GitHub, combined with SSL verification bypass to evade basic rate limits.

### ⚙️ Installation

1. Clone the repository or navigate to the project directory:
```bash
cd Day85_Omni-Recon
```

2. Create and activate a virtual environment (Recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required dependencies:
```bash
pip install requests phonenumbers urllib3
```

### 🚀 Usage

Execute the core script and follow the interactive CLI menu:

```bash
python omni_recon.py
```

### 📊 Tactical Output Example

```bash
[*] Email Breach Scan (Proxy Rotation Modu Aktif): target@email.com
[*] GitHub'dan güvenilir Proxy listesi toplanıyor...
[+] 100 adet aktif proxy IP'si mermiliğe yüklendi!
[*] Vuruş 1/10 | Kullanılan IP: 198.51.100.14:8080
[+] GİZLİLİK AŞILDI! Veriler Çekiliyor...
[!] DANGER: ŞİFRELER SIZMIŞ!
    - LinkedIn Scrape
    - Canva Data Breach
[+] Bağlı Sosyal Medya Profilleri:
    - Spotify
    - Twitter
```

---
*Developed as part of the 100 Days of Python Challenge (Day 85).*