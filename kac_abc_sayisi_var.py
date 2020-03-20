# -*- coding: utf-8 -*-

sonuc = 0
for sayid in range(100,  1000):
  on = sayid % 100
  yuz = sayid - on
  yuzd = yuz // 100
  ond = on // 10
  bir = on %10
  bird =  bir // 1
  if ond != 0 and bird != 0:
    if yuzd % ond == 0 and ond % bird==0:
      print(sayid)
      sonuc += 1
print(sonuc)