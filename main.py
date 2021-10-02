from random import choice
import requests as r

print('Sayfa Bulucu - 1.0.0\n')

c = input("Hangi Sitede Denenicek : ")
sayı = input('Kaç Kere Denenicek : ')

for x in range(int(sayı)):
   oku = list(open('txt.txt', 'r').read().splitlines())
   a = choice(oku)
   code = r.get(c + a)
   if code.status_code == 200:
    print("\033[32m" + c + a)

   if code.status_code == 429:
     print('Aşırı Fazla İstek 1 Dk Bekleyiniz')
     exit()
   if code.status_code == 404:
    print("\033[31m" + 'Sayfa Yok :' + c + a)