import random as R

class ag():
    def __init__(self,kiv,kps,kpb): # kac input var, katman pec. sifir, katman pec. bir
        self.oks = 0.0001 # ogrenme kat sayisi
        self.bias = 3
        self.kpb = kpb
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
        self.o1 = self.mulliste(giris,self.katbir)
        self.o2 = []
        for tek in self.katiki:
            self.o2.append(self.activation(sum(self.mulliste(self.o1,tek))))
        self.o3 = []
        for tek in self.katuc:
            self.o3.append(self.activation(sum(self.mulliste(self.o2,tek))))
        return self.o3

    def ogren(self,giris,cikis): # [a,b],[a,b]
        cikti0 = self.tahmin(giris)
        hata0 = [(cikis[i] - cikti0[i])**2 for i in range(self.kpb)]
        print(hata0)