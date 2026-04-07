FROM python:3.11-alpine

# Nmap ve Sudo kurulumu
RUN apk update && \
    apk add --no-cache nmap nmap-scripts sudo

# Sudo yapılandırması (şifresiz kullanım)
RUN echo "root ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Çalışma dizini oluştur
WORKDIR /app

# Önce gereksinimleri kopyala ve yükle (Cache optimizasyonu)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Tüm dosyaları kopyala
COPY . .

# Çıktıların tutulacağı klasörü oluştur
RUN mkdir -p taramalar

# Uygulamayı argümanlarla çalıştırılabilir hale getir
ENTRYPOINT ["python", "main.py"]
CMD ["-h"]
