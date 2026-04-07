import sys
import os
import unittest
import shutil

# Kod kapsamı için ana dizini dahil et
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Ayarlar
from RaporOlusturucu import rapor_yaz

class TestRaporOlusturucu(unittest.TestCase):
    def setUp(self):
        # Rapor klasörünü izole et
        self.orijinal_dizin = Ayarlar.RAPOR_DIZINI
        Ayarlar.RAPOR_DIZINI = "test_taramalar_tmp"
        if os.path.exists(Ayarlar.RAPOR_DIZINI):
            shutil.rmtree(Ayarlar.RAPOR_DIZINI)

    def tearDown(self):
        # Temizlik
        if os.path.exists(Ayarlar.RAPOR_DIZINI):
            shutil.rmtree(Ayarlar.RAPOR_DIZINI)
        Ayarlar.RAPOR_DIZINI = self.orijinal_dizin

    def test_rapor_yaz(self):
        hedef = "127.0.0.1"
        metin = "Test Nmap Çıktısı Modülü"
        
        rapor_yaz(hedef, metin)
        
        self.assertTrue(os.path.exists(Ayarlar.RAPOR_DIZINI))
        dosyalar = os.listdir(Ayarlar.RAPOR_DIZINI)
        self.assertEqual(len(dosyalar), 1)
        self.assertTrue(dosyalar[0].startswith("rapor_127.0.0.1_"))
        
        with open(os.path.join(Ayarlar.RAPOR_DIZINI, dosyalar[0]), "r", encoding="utf-8") as f:
            icerik = f.read()
            self.assertIn("Test Nmap Çıktısı Modülü", icerik)

if __name__ == '__main__':
    unittest.main()
