import time


yapilacaklar_listesi = []

kullanici_adi = input('Lütfen adınızı ve soyadınızı giriniz: ')
print(f"Hoşgeldin, {kullanici_adi}!")

while True:
    print("\nYapılacaklar Listesi Uygulaması")
    print("1. Görev Ekle")
    print("2. Görevleri Görüntüle")
    print("3. Görev Tamamlama")
    print("4. Zamanlayıcı Kur")
    print("5. Çıkış")

    secim = input("Hangi işlemi yapmak istiyorsun: (1/2/3/4/5): ")

    if secim == '1':
        yeni_gorev = input("Yeni görevi girin: ")
        yapilacaklar_listesi.append(yeni_gorev)
        print("Görev başarıyla eklendi!")
        
        dakika = int(input("Görev için hatırlatıcıyı kaç dakika sonra almak istersiniz? "))
        print(f"Hatırlatıcı {dakika} dakika sonra çalışacak.")
        time.sleep(dakika * 60)
        print("Zaman doldu! Hatırlatıcı: Yapılacaklar Listesi'ni kontrol et!")
       

    elif secim == '2':
        print("\nGörevler:")
        for indeks, gorev in enumerate(yapilacaklar_listesi, start=1):
            print(f"{indeks}. {gorev}")

    elif secim == '3':
        print("\nGörevler:")
        for indeks, gorev in enumerate(yapilacaklar_listesi, start=1):
            print(f"{indeks}. {gorev}")
        gorev_numarasi = int(input("Tamamlandı olarak işaretlemek istediğiniz görevin numarasını girin: "))
        if 1 <= gorev_numarasi <= len(yapilacaklar_listesi):
            tamamlanan_gorev = yapilacaklar_listesi.pop(gorev_numarasi - 1)
            print(f"'{tamamlanan_gorev}' görevi tamamlandı ve listeden çıkarıldı.")
        else:
            print("Geçersiz görev numarası. Lütfen tekrar deneyin.")

    elif secim == '4':
        dakika = int(input("Hatırlatıcıyı kaç dakika sonra almak istersiniz? "))
        print(f"Hatırlatıcı {dakika} dakika sonra çalışacak.")
        time.sleep(dakika * 60)
        print("Zaman doldu! Hatırlatıcı: Yapılacaklar Listesi'ni kontrol et!")

    elif secim == '5':
        print("Yapılacaklar Listesi Uygulaması kapatılıyor...")
        break

    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")

   