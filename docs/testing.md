# Test Politikası ve Fonksiyonel Testler

NmapScannerTool modüler yapısında yer alan güvenlik, işlevsellik ve arşivleme entegrasyonlarının başarılı, hatalı veya bağımsız durumlarda düzgün çalıştığını doğrulamak için tasarlanmış test belgesidir.

## 1. Sözdizimi (Syntax) ve Modüler Çalışma Testleri
Sistemin temiz bir Python ortamında çalıştığını test etmek için öncelikle sözdizim (syntax) taraması gerçekleştirilmelidir.
- **Beklenen Sonuç:** Terminalden `python3 -m py_compile ScannerTool.py` kodu çalıştırıldığında hiçbir *syntax error* veya girinti (indentation) hatası dönmemeli (Çıkış Kodu başarılı olarak, yani 0 dönmelidir).

## 2. Nmap CLI Entegrasyon Testi
- **Ağ İletişim Keşfi:** Ana panelden Cihaz Keşfi (Ping Scan) kullanılarak, `nmap -sn` parametresi modüle düzgün çekiliyor mu bakılmalıdır. Tüm komutların standart olarak `subprocess.run` üzerinden çalıştırıldığına dikkat edilmelidir.
- **Zafiyet Tespit Aracı İşletimi:** Nmap araç pakedi içerisindeki `script=vuln` argümanı ve testlerin bir problem / limitasyon olmaksızın başarıyla çağrıldığı test edilmelidir.

## 3. Rapor İzolasyon ve Analiz Testi
Çalıştırılan tarama özelliklerinin çıktıları projenin kök dizininde asılı kalmamalıdır.
- **Klasör Egzersizi:** Rapor oluşturucu, her koşuldan sonra eğer ki belirtilen (örn: `taramalar/`) klasörü eksikse dinamik olarak (os.makedirs üzerinden) dizini başlatabilmeli.
- **Log Temizliği:** Çıktılar klasör içerisine `<rapor_hedefIP_Tarih_Saat>.txt` şeklinde zaman damgasına uygun yazılarak, `ScannerTool.py` içerisinde açık kalıp dosya zehirlenmesine neden olmayacak şekilde (with open) kapatılmalıdır.

## 4. Akıllı Analiz Motoru Ayrıştırma (Regex) Testi
ScannerTool'da log dosyalarına yazılan text haldeki çıktılar işlenerek portlar ayıklanmalıdır.
- **Hedef Fonksiyon:** Nmap standardında `.../tcp open (servis)` şeklinde dönen bir liste regex marifeti ile Python belleğine liste objesi olarak kaydedilmelidir.
- **Değerlendirme Kontrolü:** Yakalanan dizideki rakam değerleri sırasıyla, `AnalizMotoru.py` içindeki öneriler sözlüğünde (Örn: HTTP için 80, SSH için 22) aranmalı ve ilgili kilit port açıksa kullanıcı asistanı arayüzünde "Ağ paylaşım izinleri ..." diyerek teknik uyarısını yansıtmalıdır.

## 5. Konteyner Testi (Docker Bildirimi)
Çalışma takımının veya değerlendiricinin projeyi birleştirilmiş (dockerize) biçimde kendi lokal işletim sisteminin kütüphanelerini kirletmeden koşturabilmesi hedeflenmiştir.
- `docker build -t nmapscanner .` komutu üzerinden bir image alınarak başarılı şekilde bir alpine dağıtımında ayağa kalktığı onaylanmalıdır.
