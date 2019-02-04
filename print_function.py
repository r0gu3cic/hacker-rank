n = int(input())
result=0
for i in range(1,n+1,1):#brojevi koji ce se redjati
    if i>=1 and i<10:
        result=result*10+i
    if i>=10 and i<100:
        result=result*100+i
        continue
    if i>=100 and i<1000:
        result=result*1000+i
        continue
    if i>=1000 and i<10000:
        result=result*10000+i
        continue
print(result)
