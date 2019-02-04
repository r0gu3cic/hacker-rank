from collections import Counter
X=int(input())#broj cipela u radnji
n=input()#string sa cipele po brojevi koje ima u radnju
m=list(map(int, n.split()))#lista sa brojevima cipela spremna za unos u recnik
dict=Counter(m)#{velicina: kolicina}
# print(dict)
N=int(input())#broj musterija
kasa=0
for i in range(N):
    velicina=0
    cena=0
    zahtev=input().split()
    velicina=int(zahtev[0])
    # print(velicina)
    cena=int(zahtev[1])
    # print(cena)
    if velicina in dict.keys():
        kolicina=dict.get(velicina, 0)
        if kolicina!=0:
            dict[velicina]=kolicina-1
            kasa+=cena
print(str(kasa))
