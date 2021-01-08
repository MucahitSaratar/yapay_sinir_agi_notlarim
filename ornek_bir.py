import random as R
sabit1 = 0.001 # ciktinin cok buyuk olmasini engeller
bias = 5
def f(a,b,c): # tahmin edilmesi istenen fonsiyon
    return (a*5+b*4+c*2+9+bias)*sabit1

o0 = f(5,8,7) # egitim icin gercek bir ciktiya ihtiyac vardır
print("gercek cikti:", o0)
bir = R.random() 
iki = R.random()
uc = R.random()
# agirliklarin rastgele dagitilmasi
for _ in range(50):
    c0 = f(bir,iki,uc) # ciktiyi hesapla
    print("duzeltme oncesi cikti : ",c0)
    hata = (o0 - c0)**2 # hatayi hesapla
    print("Hata:",hata)
    bir += 2 * (o0-c0) * -bir * sabit1 # agirligin ciktiya gore turevini al ve topla
    iki += 2 * (o0-c0) * -iki * sabit1
    uc += 2 * (o0-c0) - -uc * sabit1
    c0 = f(bir,iki,uc) # yeni agirliklar ile tekrar cikti al
    print("duzeltmeden sonraki cikit:",c0)
    print("-"*30)
