# 🛡️ NmapScannerTool: Python Tabanlı Ağ Analiz Modülü

NmapScannerTool, ağ keşfi ve güvenlik denetimi süreçlerini otomatize etmek için geliştirilmiş interaktif bir analiz aracıdır. Ham tarama verilerini, `analiz_motoru.py` üzerinden işleyerek kullanıcıya teknik tavsiyelerle sunar.

---

### 🚀 Desteklenen Tarama Türleri

Proje kapsamında aşağıdaki Nmap taramaları modüler olarak entegre edilmiştir:

* 🔍 **Standart Tarama:** Hedef IP üzerindeki temel portları ve servis durumlarını tespit eder.
* ⚙️ **Versiyon Tespiti (-sV):** Çalışan servislerin detaylı sürüm bilgilerini görüntüler.
* 💻 **OS Analizi (-O):** Hedef cihazın işletim sistemi tahminlerini analiz eder ve listeler.
* ⚡ **Hızlı Tarama (-F):** En yaygın 100 portu hızlıca tarayarak zaman tasarrufu sağlar.
* 📡 **Ping Scan (-sn):** Cihazların ağ üzerindeki aktiflik durumunu kontrol eder.
* 🧠 **Akıllı Analiz:** Tespit edilen her port için otomatik güvenlik önerileri üretir.

---

### 📂 Proje Mimarisi

| Dosya Adı | Görev |
| :--- | :--- |
| **ScannerTool.py** | Ana kullanıcı arayüzü ve Nmap komut motoru entegrasyonu. |
| **analiz_motoru.py** | Port bazlı teknik risk analizi ve çözüm önerileri modülü. |
| **.gitignore** | Gereksiz sistem dosyalarının ve logların izolasyonu. |

---

### 🛠️ Kurulum ve Kullanım

**1. Ön Gereksinim:**
Sisteminizde **Nmap** kurulu olmalıdır (`sudo apt install nmap` veya `brew install nmap`).

**2. Bağımlılıklar:**
```bash
pip3 install colorama
