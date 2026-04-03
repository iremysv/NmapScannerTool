import subprocess
import shlex
import os

def güvenli_komut_çalıştır(komut_listesi, rapor_adi):
    """
    shell=True kullanmadan, komutları liste olarak güvenli şekilde çalıştırır.
    """
    try:
        print(f"\n[+] Tarama başlatıldı: {' '.join(komut_listesi)}")
        # stdout ve stderr'i yakalayarak daha profesyonel çıktı yönetimi sağlar
        sonuc = subprocess.run(komut_listesi, capture_output=True, text=True, check=True)
        
        with open(f"{rapor_adi}.log", "w") as f:
            f.write(sonuc.stdout)
            
        print(f"[!] İşlem tamamlandı. Sonuç {rapor_adi}.log dosyasına kaydedildi.")
        return sonuc.stdout
    except subprocess.CalledProcessError as e:
        print(f"[-] Nmap hatası: {e.stderr}")
    except Exception as e:
        print(f"[-] Beklenmedik hata: {e}")

def ana_menu():
    while True:
        print("\n=== Gelişmiş Nmap Analiz Aracı ===")
        print("1- Standart Tarama\n2- Versiyon Tespiti\n3- Çıkış")
        
        secim = input("\nSeçiminiz: ")
        if secim == "3": break
        
        hedef = input("Hedef IP (Örn: 192.168.1.1): ")
        
        # Basit Input Validation
        if not hedef.replace(".", "").isalnum():
            print("[-] Geçersiz hedef formatı!")
            continue

        if secim == "1":
            güvenli_komut_çalıştır(["nmap", hedef], "standart_tarama")
        elif secim == "2":
            güvenly_komut_çalıştır(["nmap", "-sV", hedef], "versiyon_tarama")

if __name__ == "__main__":
    ana_menu()
