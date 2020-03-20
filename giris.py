# -*- coding: utf-8 -*-

import random
import time

print("Sitemize hoşgeldiniz!")
print(" ")
time.sleep(0.5)

badeger = 0
kayitsayisi = 0
kullanicilar = []
sifreleri = []

while True:
    if(badeger ==3):
        print("Deneme hakkınız doldu")
        break
    else:
        print("Lütfen yapmak istediğiniz işlemi seçiniz")
        time.sleep(0.5)
        print("[1]Kayıt Ol")
        time.sleep(0.5)
        print("[2]Giriş Yap")
        time.sleep(0.5)
        print("[3]Şifremi Unuttum")
        time.sleep(0.5)
        print("[4]Çıkış Yap")
        time.sleep(0.5)
        secim = int(input("> "))
        if(secim == 1):
            kayitkadi = input("Kullanıcı Adı: ")
            while True:
                if(kullanicilar.count(kayitkadi) == 1):
                    print("Bu ad kullanılmaktadır. Lütfen başka bir kullanıcı adı seçiniz.")
                    print(" ")
                else:
                    kullanicilar.append(kayitkadi)                
                    kayitsifre = input("Şifreniz: ")
                    sifreleri.append(kayitsifre)
                    print("Bilgileriniz başarı ile kaydedilmiştir.")
                    print(" ")
                    kayitsayisi += 1
                    break
        elif(secim ==2):
            print(3-badeger,"hakkınız kaldı" )
            kad = str(input("Kullanıcı Adınızı Giriniz: "))
            if(kullanicilar.count(kad) == 1):
                sbilgi = str(input("Lütfen Şifrenizi Giriniz: "))
                sira = kullanicilar.index(kad)
                sifsira = sifreleri[sira]
                if(sifsira == sbilgi):
                    print("Başarıyla giriş yapıldı.")
                    print("")
                    print("Ne yapmak istiyorsunuz?")
                    print("[<1]Çıkış yap")
                    print("[2<]Giriş sayfasına dön")
                    secimgirdi = float(input("> "))
                    if secimgirdi == 1 or secimgirdi < 1:
                        print("İşleminiz onaylandı")
                        time.sleep(1)
                        break
                    elif secimgirdi == 2 or secimgirdi > 2:
                        print("İşlem onaylandı")
                        print(" ")
                        time.sleep(1)
                else:
                    print("Bilgileriniz yanlıştır")
                    print("Lütfen verilen kodu giriniz:  ")
                    kod = random.randint(10000,99999)
                    print(kod)
                    a = float(input("Lütfen bu sayıyı giriniz"))
                    if a == kod:
                        badeger += 1
                    else:
                        break
            else:
                print("Böyle bir kullanıcı adı bulunmamaktadır!")
                print("Lütfen tekrar deneyiniz.")
                badeger += 1
        elif(secim == 3):
           koddegeri2 = 0
           while True:
               if koddegeri2 == 3:
                   print("Deneme hakkınız doldu.")
                   break
               else:
                   print("Lütfen verilen kodu giriniz:  ")
                   kod = random.randint(10000,99999)
                   print(kod)
                   a = float(input("Lütfen bu sayıyı giriniz: "))
                   if a == kod:
                       while True:
                           slakadi = input("Kullanıcı adınızı giriniz: ")
                           if(kullanicilar.count(slakadi) == 0):
                               print("Böyle bir kullanıcı adı bulunmamaktadır. Lütfen tekrar deneyiniz.")
                               print(" ")
                           elif(kullanicilar.count(slakadi) == 1):
                               break
                               
                       yenisifre = input("Lütfen yeni şifrenizi giriniz: ") 
                       yenisira = kullanicilar.index(slakadi)
                       sifreleri[yenisira] = yenisifre
                       print("Şifreniz başarı ile değiştirildi.")
                       print(" ")
                       break
                   else:    
                       koddegeri2 += 1 
        elif(secim == 4):
            break
        elif(secim < 0 or secim > 4):
            print("Lütfen geçerli bir işlem seçiniz.")
            badeger += 1
print("Sistemden çıkış yapılmıştır.")