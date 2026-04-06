# Değişiklik Günlüğü (Changelog)

Bütün önemli mimari ilerlemeler ve hata düzeltmeleri bu dosyada belgelenmektedir. Sürüm takibi profesyonel proje geliştirme yaklaşımına uygun olarak tutulmaktadır.

## [v1.1.0] - Güncel Bakım Sürümü
- **Eklendi:** Açık kaynak kodlu paylaşım ve telif yönetimi için MIT `LICENSE` dosyası projeye dahil edildi.
- **Eklendi:** Çeşitli ortamlarda izole test koşturmaları yapabilmek ve bağımlılıkları kolay çözmek için `Dockerfile` oluşturuldu.
- **Eklendi:** İşletim sistemleri arası LF/CRLF (Satır atlama) farklılıklarını çözmek için `.gitattributes` yapılandırıldı.
- **Eklendi:** Değerlendirme sistemleri için `architecture.md`, `changelog.md` ve `testing.md` dosyalarını barındıran teknik bir `/docs` klasörü açıldı.
- **Entegre Edildi:** `ScannerTool.py` ayrık duran modül ve servisleri kendisine referans alarak tam bağlama yapıldı. Taramadan çıkan veriler tüm sistem boyunca iletildi.
- **Entegre Edildi:** Program regex yapısıyla güçlendirildi, Nmap portları ekrandan ayrıştırılıp Akıllı Analiz Motoruna otomatik paslanabilir hale getirildi.
- **Düzeltildi:** `RaporOlusturucu.py` dosyası artık hard-coded (sabit) kök dizin yazımı yerine dinamik olarak `Ayarlar.py`'deki dizin bilgisine göre kendi klasörünü güvenli oluşturuyor.
- **Düzeltildi:** `AnalizMotoru.py` dosyasındaki SMB alanında bulunan "izinghcghfcfghleri" şeklinde basılan string/yazılım hatası ("izinleri") olarak düzeltildi.

## [v1.0.0] - İlk Modüler Sürüm
- **Güvenlik İyileştirmesi:** `os.system` kullanımındaki güvenlik açıkları ve zafiyetler `subprocess` kütüphanesi kullanılarak giderildi.
- **Mimarileştirme:** Yapıyı sadece tek bir main doyasına hapsetmeyip, işbölümü amacıyla `AnalizMotoru`, `Ayarlar`, `RaporOlusturucu`, `ZafiyetTarayici` python servisleri yaratıldı.
- **Arayüz:** Temel CLI (Terminal) işlevi gören 7 seçenekli ana menü kodlandı.
- **Gizlilik Teyidi:** Veri ihlalini engellemek için projenin kök dizinine, git gönderimlerini filtreleyen güçlü bir `.gitignore` eklendi.
