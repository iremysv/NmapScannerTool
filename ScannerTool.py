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
        print("\n" + "="*30)
        print("   NMAP TARAMA VE ANALİZ ARACI   ")
        print("="*30)
        print("1- Hızlı Tarama (-F)")
        print("2- Detaylı/Agresif Tarama (-A)")
        print("3- Zafiyet Taraması (Scripts)")
        print("4- Çıkış")
        print("="*30)
        
        secim = input("\nSeçiminiz: ")
        
        if secim == "4":
            print("[*] Program kapatılıyor...")
            break
            
        hedef = input("Hedef IP veya Domain: ")
        if not hedef: continue

        if secim == "1":
            # -F: En yaygın 100 portu çok hızlı tarar
            nmap_calistir(["nmap", "-F", hedef], "hizli_tarama")
        elif secim == "2":
            # -A: OS tespiti, versiyon tespiti ve script taraması yapar (Çok detaylıdır)
            print("[!] Bilgi: Bu işlem biraz uzun sürebilir...")
            nmap_calistir(["nmap", "-A", hedef], "detayli_analiz")
        elif secim == "3":
            try:
                from zafiyet_tarayici import zafiyet_tara
                sonuc = zafiyet_tara(hedef)
                print(sonuc)
            except ImportError:
                print("[-] Hata: zafiyet_tarayici.py bulunamadı!")
        else:
            print("[-] Geçersiz seçim.")

if __name__ == "__main__":
    ana_menu()
