import os

def nmap_calistir(komut, rapor_adi):
    print(f"\n--- Çalıştırılıyor: {komut} ---")
    os.system(f"{komut} -oN {rapor_adi}.log")
    print(f"İşlem tamamlandı. Sonuç '{rapor_adi}.log' dosyasına kaydedildi.")

def ana_menu():
    while True:
        print("\n=== AĞ TARAMA VE ANALİZ ARACI ===")
        print("1- Standart IP Taraması (nmap <ip>)")
        print("2- Web Sitesi Taraması (nmap <url>)")
        print("3- Servis ve Versiyon Tespiti (-sV)")
        print("4- İşletim Sistemi Tespiti (-O)")
        print("5- Ping Taraması / Cihaz Keşfi (-sn)")
        print("6- Çıkış")
        
        secim = input("\nSeçiminiz: ")
        if secim == "6": break
        hedef = input("Hedef IP veya URL giriniz: ")
        
        if secim == "1": nmap_calistir(f"nmap {hedef}", "ip_tarama")
        elif secim == "2": nmap_calistir(f"nmap {hedef}", "site_tarama")
        elif secim == "3": nmap_calistir(f"nmap -sV {hedef}", "servis_tespiti")
        elif secim == "4": nmap_calistir(f"sudo nmap -O {hedef}", "os_tespiti")
        elif secim == "5": nmap_calistir(f"nmap -sn {hedef}", "ping_tarama")

if __name__ == "__main__":
    ana_menu()