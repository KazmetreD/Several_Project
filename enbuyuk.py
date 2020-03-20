# -*- coding: utf-8 -*-

sayi1 = int(input("1.Sayı: "))
sayi2 = int(input("2.Sayı: "))
sayi3 = int(input("3.Sayı: "))

if sayi1 > sayi2 and sayi1 > sayi3:
    print(sayi1,"en büyük sayıdır.")
elif sayi2 > sayi1 and sayi2 > sayi3:
    print(sayi2,"en büyük sayıdır.")
else:
    print(sayi3,"en büyük sayıdır.")