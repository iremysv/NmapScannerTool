FROM python:3.11-alpine

# Nmap kurulumu
RUN apk update && \
    apk add --no-cache nmap nmap-scripts

# Çalışma dizini oluştur
WORKDIR /app

# Dosyaları kopyala
COPY . .

# Uygulamayı çalıştır
CMD ["python", "ScannerTool.py"]
