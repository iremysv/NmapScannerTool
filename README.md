# 🛡️ NmapScannerTool: Gelişmiş Ağ Analiz ve Güvenlik Çözümü

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python) ![Nmap](https://img.shields.io/badge/Tools-Nmap-orange?style=flat-square) ![License](https://img.shields.io/badge/License-MIT-green?style=flat-square) ![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

**Üniversite Adı:** İstinye Üniversitesi  
**Danışman/Eğitmen:** Keyvan Arasteh Abbasabad  
**Geliştirici:** İrem Yasav

NmapScannerTool; ağ keşfi, servis analizi ve zafiyet tespiti süreçlerini modüler bir yapıda otomatize eden Python tabanlı bir güvenlik aracıdır. Proje, sadece tarama yapmakla kalmaz; tespit edilen bulguları anlamlandırarak teknik raporlar üretir.

---

## 📑 İçindekiler
- [Demo](#-demo)
- [Özellikler](#-özellikler)
- [Proje Mimarisi](#-proje-mimarisi-modüler-yapı)
- [Kurulum ve Kullanım](#️-kurulum-ve-kullanım)

---

## 🎬 Demo
Aşağıdaki animasyonda `main.py` üzerinden kurulum, yardım menüsü, hızlı tarama, cihaz keşfi ve mimari analizi (wc -l) barındıran 3.5 dakikalık kapsamlı (*comprehensive*) demo senaryosunu izleyebilirsiniz:

![NmapScannerTool Demo](demo/project-demo.webm)

---

### 🚀 Özellikler

* 🔍 **Standart Tarama:** Hedef IP üzerindeki temel portları ve servis durumlarını tespit eder.
* ⚙️ **Versiyon Tespiti (-sV):** Çalışan servislerin detaylı sürüm bilgilerini görüntüler.
* 💻 **OS Analizi (-O):** Hedef cihazın işletim sistemi tahminlerini analiz eder ve listeler.
* ⚡ **Hızlı Tarama (-F):** En yaygın 100 portu hızlıca tarayarak zaman tasarrufu sağlar.
* 📡 **Ping Scan (-sn):** Cihazların ağ üzerindeki aktiflik durumunu kontrol eder.
* 🧠 **Akıllı Analiz Motoru:** Açık portlar için otomatik güvenlik sıkılaştırma önerileri üretir.
* 📂 **Otomatik Raporlama:** Tüm tarama sonuçlarını tarih damgalı `.txt` dosyaları olarak arşivleme.
* 🛡️ **Zafiyet Tarama:** Nmap Script Engine (NSE) entegrasyonu ile zafiyet keşfi.
* ⚙️ **Merkezi Yapılandırma:** Tarama hızını ve parametrelerini tek bir dosyadan yönetme kolaylığı.

---

### 📂 Proje Mimarisi (Modüler Yapı)

Proje, sürdürülebilir kod prensiplerine uygun olarak aşağıdaki bileşenlere ayrılmıştır:

| Dosya Adı | Görev |
| :--- | :--- |
| **main.py**          | CLI arayüzü ve merkezi uygulama girişi. |
| **ScannerTool.py**   | Nmap süreç yönetimi ve tarama fonksiyonları. |
| **AnalizMotoru.py**  | Port bazlı teknik risk analizi ve çözüm önerileri. |
| **Ayarlar.py**       | Tarama hızı ve dizin ayarlarının yönetimi. |
| **RaporOlusturucu.py**| Tarama sonuçlarının .txt formatında raporlanması. |
| **ZafiyetTarayici.py**| Hassas dizin ve zafiyet tarama modülü. |
| **.gitignore** | Gereksiz sistem dosyalarının izolasyonu. |

---

### 🛠️ Kurulum ve Kullanım

**1. Gereksinimler:** Sistemenizde **Nmap** kurulu olmalıdır (`sudo apt install nmap` / `brew install nmap`).
**2. Kütüphaneler:** Renkli çıktılar için `pip3 install colorama` komutunu çalıştırın.
**3. Çalıştırma:** ```bash
   python3 ScannerTool.py
