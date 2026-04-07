# Katkıda Bulunma Rehberi (Contributing)

NmapScannerTool projesine ilgi duyduğunuz ve katkıda bulunmak istediğiniz için teşekkür ederiz! Lütfen aşağıdaki adımları takip ederek süreci herkes için daha verimli hale getirin.

## Nasıl Katkıda Bulunabilirsiniz?

1. **Bug Bildirimi:** Karşılaştığınız hataları veya sorunları Issue olarak açabilirsiniz.
2. **Özellik Talebi:** Projeye eklenebilecek yeni tarama modları veya analiz yöntemleri önerebilirsiniz.
3. **Kod Katkısı:** Doğrudan kodu geliştirerek veya dokümantasyonu iyileştirerek katkı sağlayabilirsiniz.

## Geliştirme Süreci

1. Bu depoyu kendi hesabınıza "Fork" edin.
2. Yerel ortamınızda yeni bir dal (branch) oluşturun: `git checkout -b feature/YeniOzellik` veya `git checkout -b fix/HataCozumu`
3. Değişikliklerinizi yapın ve anlamlı commit mesajları yazın.
4. Dalınızı kendi deponuza yükleyin: `git push origin feature/YeniOzellik`
5. Ana depoya bir Pull Request (PR) açın.

## Kod Standartları

- Python PEP-8 standartlarına olabildiğince uygun kod yazmaya çalışın.
- Eklediğiniz yeni modüller için açıklayıcı (docstring) yorumlar eklemeyi unutmayın.
- Yeni paketler eklediyseniz `requirements.txt` dosyasını güncelleyin.
