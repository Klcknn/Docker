FROM ubuntu
RUN apt-get update -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install flask
COPY . /app
WORKDIR /app
CMD python3 ./welcome.py


# Bu bir Dockerfile adlı dosyanın içeriğini temsil eder. Dockerfile, bir Docker konteyneri oluşturmak için kullanılan bir dosyadır. İşte bu Dockerfile'daki her komutun ne yaptığının açıklamaları:

# FROM ubuntu: Bu komut, Docker konteynerinizin temel imajını belirler. Bu Docker konteyneri, Ubuntu işletim sistemi üzerine kurulu olacak.

# RUN apt-get update -y: Bu komut, Ubuntu paket yöneticisi olan APT'yi kullanarak sistemdeki paketlerin güncellenmesini sağlar. -y bayrağı, güncelleme işleminin otomatik onay almasını sağlar.

# RUN apt-get install python3 -y: Bu komut, Python 3'ü Ubuntu üzerinde yükler. Yine -y bayrağı, yükleme işlemi sırasında herhangi bir onay gerektirmeyeceğini belirtir.

# RUN apt-get install python3-pip -y: Bu komut, Python 3 için paket yöneticisi olan pip'i yükler. Yine -y bayrağı, onay gerektirmeyen bir kurulumu temsil eder.

# RUN pip3 install flask: Bu komut, Python 3 için Flask adlı bir web uygulaması çerçevesini yükler. Flask, web uygulamaları geliştirmek için kullanılır.

# COPY . /app: Bu komut, Dockerfile'ın bulunduğu dizindeki tüm dosyaları (.) Docker konteynerinin içindeki /app dizinine kopyalar. Bu, Docker konteynerine uygulama kodunun eklenmesini sağlar.

# WORKDIR /app: Bu komut, çalışma dizinini (WORKDIR) Docker konteynerinin içinde /app dizini olarak ayarlar. Bu, sonraki komutların bu dizin içinde çalışmasını sağlar.

# CMD python3 ./welcome.py: Bu komut, Docker konteyneri başladığında otomatik olarak çalışacak komutu belirler. Bu komut, /app dizinindeki welcome.py adlı Python betiğini çalıştırır.

# Sonuç olarak, bu Dockerfile, Ubuntu tabanlı bir Docker konteyneri oluşturur, içine Python 3, pip ve Flask kurar, ardından bir Flask uygulamasını içeren bir dizini konteynerin içine kopyalar ve bu uygulamayı çalıştırır. 
# Bu, bir Flask web uygulamasını Docker konteynerinde çalıştırmak için kullanılabilir.






