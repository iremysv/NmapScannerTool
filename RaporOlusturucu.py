# -*- coding: utf-8 -*-
import os
from datetime import datetime

def rapor_yaz(hedef, sonuc_metni):
    tarih = datetime.now().strftime("%Y-%m-%d_%H-%M")
    dosya_adi = f"rapor_{hedef}_{tarih}.txt"
    
    with open(dosya_adi, "w", encoding="utf-8") as f:
        f.write(f"--- NMAP TARAMA RAPORU ---\n")
        f.write(f"Hedef: {hedef}\n")
        f.write(f"Tarih: {tarih}\n")
        f.write("-" * 30 + "\n")
        f.write(sonuc_metni)
    
    print(f"\n[+] Rapor başarıyla oluşturuldu: {dosya_adi}")
