# Proje Mimarisi (NmapScannerTool)

NmapScannerTool, sürdürülebilir yazılım prensiplerini baz alarak ayrıştırılmış modüler bir yapı sunar. 

## Bileşenler

- **`ScannerTool.py` (Main)**: Araç buradaki CLI arayüzü ile tetiklenir. Kullanıcı girdisine göre Nmap komutlarını dinamikleştirip, `subprocess` üzerinden işletim sistemine aktarır. Nmap çıktısından Regex ile elde edilen sonuçları, iş akışına göre Raporlama ve Analiz Motoruna yönlendirir.
- **`Ayarlar.py`**: Sistemin hız (`-T4`), çıktı dizini (`taramalar/`) gibi değişkenlerinin hard-coded (sabit kod) olarak kod içinde kalmasını engelleyen, projenin merkezi yapılandırma havuzudur.
- **`RaporOlusturucu.py`**: Zaman damgalı metin raporları üretir. İzolasyonu sağlamak amacıyle alınan logları kök dizine bırakmak yerine güvenli şekilde spesifik bir klasörde toplar.
- **`AnalizMotoru.py`**: Nmap tarafından `open` (açık) olarak işaretlenmiş port listesini alıp, teknik güvenlik ve yapılandırma tavsiyeleri üreten akıllı analiz asistanıdır.
- **`ZafiyetTarayici.py`**: Nmap NSE (Nmap Scripting Engine) içerisindeki `vuln` klasörünü ve otomatize scriptlerini kullanarak, zafiyet tarama sürecini ayrıştırılmış şekilde yürütür.

## Veri Akışı

1. Kullanıcıdan hedef IP ve işlem tipi (1-6) istenir.
2. `Ayarlar` modülü okutularak hedeflenen terminal komutu oluşturulur.
3. Çıktılar öncelikle `RaporOlusturucu` mekanizmasına iletilerek `taramalar/` (veya ayarlardaki özel dizin) klasörüne arşivlenir.
4. Ağda iletişimde olan yani açık bulunan port sayıları Regex kullanılarak dinamik şekilde ayrıştırılır ve liste değişkeni olarak `AnalizMotoru`'na işlenmek üzere aktarılır.
