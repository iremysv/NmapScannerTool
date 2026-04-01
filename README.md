# 🛡️ NmapScannerTool: Gelişmiş Ağ Analiz ve Güvenlik Çözümü

NmapScannerTool; ağ keşfi, servis analizi ve zafiyet tespiti süreçlerini modüler bir yapıda otomatize eden Python tabanlı bir güvenlik aracıdır. Proje, sadece tarama yapmakla kalmaz; tespit edilen bulguları anlamlandırarak teknik raporlar üretir.

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
| **ScannerTool.py** | Ana kullanıcı arayüzü ve Nmap süreç yönetimi. |
| **analiz_motoru.py** | Port bazlı teknik risk analizi ve çözüm önerileri modülü. |
| **ayarlar.py** | Tarama hızı ve dizin ayarlarının merkezi yönetimi. |
| **rapor_olusturucu.py**| Tarama sonuçlarının .txt formatında raporlanması. |
| **zafiyet_tarayici.py**| Hassas dizin ve zafiyet tarama scriptleri modülü. |
| **.gitignore** | Gereksiz sistem dosyalarının izolasyonu. |

---

### 🛠️ Kurulum ve Kullanım

**1. Gereksinimler:** Sistemenizde **Nmap** kurulu olmalıdır (`sudo apt install nmap` / `brew install nmap`).
**2. Kütüphaneler:** Renkli çıktılar için `pip3 install colorama` komutunu çalıştırın.
**3. Çalıştırma:** ```bash
   python3 ScannerTool.py
