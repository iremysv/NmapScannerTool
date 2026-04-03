# -*- coding: utf-8 -*-
import subprocess

def nmap_calistir(komut_listesi, rapor_adi):
    try:
        print(f"\n[+] İşlem başlatıldı: {' '.join(komut_listesi)}")
        sonuc = subprocess.run(komut_listesi, capture_output=True, text=True, check=True)
        with open(f"{rapor_adi}.log", "w", encoding="utf-8") as f:
            f.write(sonuc.stdout)
        print(f"[!] Tarama tamamlandı. Rapor: {rapor_adi}.log")
        return sonuc.stdout
    except Exception as e:
        print(f"[-] Hata oluştu: {e}")

def ana_menu():
    while True:
        print("\n" + "="*45)
        print("      SIZMA TESTİ VE ANALİZ PANELİ      ")
        print("="*45)
        print("1- Hızlı Tarama (-F) [Top 100 Port]")
        print("2- Cihaz Keşfi (-sn) [Ping Scan]")
        print("3- Servis Versiyon Tespiti (-sV)")
        print("4- İşletim Sistemi Analizi (-O)")
        print("5- Agresif Tarama (-A) [Hepsi Bir Arada]")
        print("6- Zafiyet Taraması (NSE Scripts)")
        print("7- Çıkış")
        print("="*45)
        secim = input("\nSeçiminiz (1-7): ")
        if secim == "7": 
            print("[*] Program kapatılıyor. İyi çalışmalar İrem!")
            break
        hedef = input("Hedef IP veya Domain: ")
        if not hedef: continue
        if secim == "1":
            nmap_calistir(["nmap", "-F", hedef], "hizli_tarama")
        elif secim == "2":
            nmap_calistir(["nmap", "-sn", hedef], "cihaz_kesfi")
        elif secim == "3":
            nmap_calistir(["nmap", "-sV", hedef], "servis_analizi")
        elif secim == "4":
            nmap_calistir(["sudo", "nmap", "-O", hedef], "os_analizi")
        elif secim == "5":
            nmap_calistir(["sudo", "nmap", "-A", hedef], "agresif_tarama")
        elif secim == "6":
            try:
                from ZafiyetTarayici import zafiyet_tara
                sonuc = zafiyet_tara(hedef)
                print(sonuc)
            except ImportError:
                print("[-] Hata: ZafiyetTarayici.py bulunamadı!")
        else:
            print("[-] Geçersiz seçim.")

if __name__ == "__main__":
    ana_menu()
