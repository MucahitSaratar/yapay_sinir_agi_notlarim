import random as R

class ag():
    def __init__(self,kiv,kps,kpb): # kac input var, katman pec. sifir, katman pec. bir
        self.oks = 0.5 # ogrenme kat sayisi
        self.bias = 3
        self.kpb = kpb
        self.kps = kps
        self.kiv = kiv
        self.katbir = [R.random() for i in range(kiv)]
        self.katiki = [[R.random() for a in range(kiv)] for i in range(kps)]
        self.katuc = [[R.random() for i in range(kps)] for a in range(kpb)]

    def mulliste(self,bir,iki):
        try:
            assert len(bir) == len(iki)
        except:
            print(f"bir: {len(bir)}  -  iki: {len(iki)}")
        return [bir[i] * iki[i] for i in range(len(bir))]

    def activation(self,x):
        return 0.006 * x

    def tahmin(self,giris):
        self.giris = giris
        self.o1 = self.mulliste(self.giris,self.katbir)
        self.o2 = []
        for tek in self.katiki:
            self.o2.append(self.activation(sum(self.mulliste(self.o1,tek))))
        self.o3 = []
        for tek in self.katuc:
            self.o3.append(self.activation(sum(self.mulliste(self.o2,tek))))
        return self.o3

    def ogren(self,giris,cikis,ts=100): # [a,b],[a,b]
        for tekrar in range(ts):
            cikti0 = self.tahmin(giris)
            self.degisken = cikti0
            hatalar = [(cikis[i] - cikti0[i])**2 for i in range(self.kpb)]
            self.hata = hatalar
            for sayi0 in range(self.kpb):
                hhm = cikis[sayi0] - cikti0[sayi0] # hep hesaplama
                for ins in range(self.kiv):
                    for lan in range(self.kps):
                        self.katbir[ins] += 2 * hhm * self.katuc[sayi0][lan]  * self.katiki[lan][ins] * self.giris[ins] * self.oks * 0.006**2
                for iks in range(self.kps):
                    for i in range(self.kiv):
                        self.katiki[iks][i] += 2 * hhm * self.katuc[sayi0][iks] * self.o1[i] * self.oks * 0.006**2
                for bol in range(self.kps):
                    self.katuc[sayi0][bol] += 2 * hhm * self.o2[bol] * self.oks * 0.006
