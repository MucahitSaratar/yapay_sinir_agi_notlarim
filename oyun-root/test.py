import ysa
ag = ysa.ag(4,6,3)

i0 = [1,2,3,4]
c0 = [0,1,1]

ag.ogren(i0,c0,1)
print("Hata: ",ag.hata)
print("cikti: ",ag.degisken)
ag.ogren(i0,c0,6000)
print("Hata: ",ag.hata)
print("cikti: ",ag.degisken)

