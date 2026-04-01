# -*- coding: utf-8 -*-
import subprocess

def dizin_tara(target_url):
    print(f"\n[!] {target_url} için hassas dizin taraması başlatılıyor...")
    # Basit bir brute force simülasyonu veya nmap script kullanımı
    # Örnek: nmap --script http-enum
    try:
        cmd = f"nmap --script http-enum {target_url}"
        sonuc = subprocess.check_output(cmd, shell=True).decode()
        return sonuc
    except:
        return "Zafiyet taraması sırasında bir hata oluştu."
