import requests
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import time
from concurrent.futures import ThreadPoolExecutor
import random
import urllib3

# SSL uyarılarını terminalde görmemek için susturuyoruz
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Terminal color codes
G = '\033[92m'  # Green
R = '\033[91m'  # Red
Y = '\033[93m'  # Yellow
W = '\033[0m'   # Reset

def print_banner():
    print(f"""{G}
   ____                  _       ____                     
  / __ \____ ___  ____  (_)     / __ \___  _________  ____ 
 / / / / __ `__ \/ __ \/ /_____/ /_/ / _ \/ ___/ __ \/ __ \\
/ /_/ / / / / / / / / / /_____/ _, _/  __/ /__/ /_/ / / / /
\____/_/ /_/ /_/_/ /_/_/     /_/ |_|\___/\___/\____/_/ /_/ 
    
        [+] OSINT Digital Footprint & Breach Scanner v3.2 [+]
        [+] Features: Multithreading & GitHub Proxy Rotation [+]
        [+] Target: IP | Username | Phone | Email [+]
{W}""")

def scan_ip(ip_address):
    print(f"\n{Y}[*] IP & Geo-Location Recon: {ip_address}{W}")
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}").json()
        if response['status'] == 'success':
            print(f"{G}[+] Country: {response['country']} ({response['countryCode']}){W}")
            print(f"{G}[+] City/Region: {response['city']} / {response['regionName']}{W}")
            print(f"{G}[+] ISP/Org: {response['isp']} / {response['org']}{W}")
            print(f"{G}[+] Timezone: {response['timezone']}{W}")
            print(f"{G}[+] Coordinates: {response['lat']}, {response['lon']}{W}")
        else:
            print(f"{R}[-] IP resolve error.{W}")
    except Exception as e:
        print(f"{R}[-] Exception: {e}{W}")

def scan_phone(phone_number):
    print(f"\n{Y}[*] Advanced Telecom Recon: {phone_number}{W}")
    try:
        parsed_number = phonenumbers.parse(phone_number)
        if phonenumbers.is_valid_number(parsed_number):
            region = geocoder.description_for_number(parsed_number, "en")
            isp = carrier.name_for_number(parsed_number, "en")
            t_zone = timezone.time_zones_for_number(parsed_number)
            
            n_type = phonenumbers.number_type(parsed_number)
            type_str = "Mobile" if n_type == 1 else "Fixed Line" if n_type == 0 else "Unknown"

            print(f"{G}[+] Valid Number: True{W}")
            print(f"{G}[+] Location: {region}{W}")
            print(f"{G}[+] Carrier: {isp if isp else 'Unknown'}{W}")
            print(f"{G}[+] Line Type: {type_str}{W}")
            print(f"{G}[+] Timezone: {t_zone}{W}")
            print(f"{G}[+] National Format: {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)}{W}")
        else:
             print(f"{R}[-] Invalid phone number!{W}")
    except Exception as e:
        print(f"{R}[-] Parse error: {e}{W}")

def check_platform(platform, url, headers):
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            if url.split('/')[-1].lower() in response.text.lower():
                return f"{G}[+] FOUND! [{platform}]: {url}{W}"
        return None
    except:
        return None

def scan_username(username):
    print(f"\n{Y}[*] Multithreaded Digital Footprint Scan: {username}{W}")
    
    platforms = {
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}/",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "TryHackMe": f"https://tryhackme.com/p/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "HackTheBox": f"https://www.hackthebox.eu/profile/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}/",
        "Vimeo": f"https://vimeo.com/{username}",
        "Twitch": f"https://www.twitch.tv/{username}"
    }
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(check_platform, p, u, headers) for p, u in platforms.items()]
        for future in futures:
            result = future.result()
            if result:
                print(result)

def get_free_proxies():
    """GitHub üzerindeki güvenilir bir repodan anlık bedava proxy listesi çeker."""
    print(f"\n{Y}[*] GitHub'dan güvenilir Proxy listesi toplanıyor...{W}")
    # Hedef Değişti: GitHub Raw Verisi
    url = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"
    
    try:
        # SSL Bypass aktif
        response = requests.get(url, timeout=10, verify=False)
        proxies = response.text.strip().split('\n')
        proxies = [p.strip() for p in proxies if p.strip()] 
        
        # Dosyada on binlerce proxy olabilir, belleği yormamak için rastgele 100 tanesini alıyoruz
        if len(proxies) > 100:
            proxies = random.sample(proxies, 100)
            
        print(f"{G}[+] {len(proxies)} adet aktif proxy IP'si mermiliğe yüklendi!{W}")
        return proxies
    except Exception as e:
        print(f"{R}[-] Proxy listesi çekilemedi: {e}{W}")
        return []

def scan_email(email):
    print(f"\n{Y}[*] Email Breach Scan (Proxy Rotation Modu Aktif): {email}{W}")
    
    proxies_list = get_free_proxies()
    if not proxies_list:
        print(f"{R}[-] Proxy havuzu boş olduğu için işlem iptal edildi.{W}")
        return

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    url = f"https://emailrep.io/{email}"
    
    max_retries = 10 # Şansımızı artırmak için deneme sayısını 10'a çıkardım
    
    for attempt in range(max_retries):
        current_proxy = random.choice(proxies_list)
        proxy_dict = {
            "http": f"http://{current_proxy}",
            "https": f"http://{current_proxy}"
        }
        
        print(f"{Y}[*] Vuruş {attempt + 1}/{max_retries} | Kullanılan IP: {current_proxy}{W}")
        
        try:
            response = requests.get(url, headers=headers, proxies=proxy_dict, timeout=8, verify=False)
            
            if response.status_code == 200:
                print(f"{G}[+] GİZLİLİK AŞILDI! Veriler Çekiliyor...{W}")
                data = response.json()
                details = data.get('details', {})
                
                reputation = data.get('reputation', 'Unknown')
                rep_color = R if reputation in ['high', 'suspicious'] else G
                print(f"{rep_color}[+] Domain Reputation: {reputation.upper()}{W}")
                
                credentials_leaked = details.get('credentials_leaked', False)
                if credentials_leaked:
                    print(f"\n{R}[!] DANGER: ŞİFRELER SIZMIŞ!{W}")
                    breaches = details.get('data_breaches', [])
                    for breach in breaches:
                        print(f"    - {breach}")
                else:
                     print(f"\n{G}[+] TARGET IS CLEAN: Bilinen bir veri sızıntısı yok.{W}")

                profiles = details.get('profiles', [])
                if profiles:
                    print(f"\n{Y}[+] Bağlı Sosyal Medya Profilleri:{W}")
                    for profile in profiles:
                        print(f"    - {G}{profile.capitalize()}{W}")
                else:
                     print(f"\n{Y}[-] Açık kaynaklarda bu maile bağlı profil bulunamadı.{W}")
                
                return 

            elif response.status_code == 429:
                 print(f"{R}[-] Bu IP rate limit yemiş. Silah değiştiriliyor...{W}")
            else:
                print(f"{R}[-] Başarısız HTTP Kodu: {response.status_code}{W}")

        except requests.exceptions.ProxyError:
            print(f"{R}[-] Proxy bağlantıyı reddetti. Başka IP aranıyor...{W}")
        except requests.exceptions.Timeout:
            print(f"{R}[-] Proxy çok yavaş (Zaman Aşımı). Başka IP aranıyor...{W}")
        except requests.exceptions.ConnectionError:
            print(f"{R}[-] Proxy bağlantısı koptu. Başka IP aranıyor...{W}")
        except Exception as e:
            print(f"{R}[-] Beklenmeyen Proxy Hatası. Başka IP aranıyor...{W}")
            
    print(f"\n{R}[!] Operasyon Başarısız: {max_retries} farklı IP denendi ama hepsi ölü veya engelli çıktı.{W}")

def main():
    print_banner()
    while True:
        print(f"\n{Y}=== HEDEF SEÇİMİ ==={W}")
        print("1. IP & Geo-Location Scan")
        print("2. Username Digital Footprint Scan")
        print("3. Phone Number Advanced Scan")
        print("4. Email Breach & Reputation Scan (GitHub Proxy Modeli)")
        print("5. Exit")
        
        choice = input(f"\n{G}[?] İşlem Seçin (1-5): {W}")
        
        if choice == '1':
            ip = input(f"{Y}Target IP: {W}")
            scan_ip(ip)
        elif choice == '2':
            user = input(f"{Y}Target Username: {W}")
            scan_username(user)
        elif choice == '3':
            phone = input(f"{Y}Target Phone (+90 formatında): {W}")
            scan_phone(phone)
        elif choice == '4':
            email = input(f"{Y}Target Email: {W}")
            scan_email(email)
        elif choice == '5':
            print(f"{G}[*] Omni-Recon Terminated...{W}")
            break
        else:
            print(f"{R}[-] Invalid Input!{W}")

if __name__ == "__main__":
    main()