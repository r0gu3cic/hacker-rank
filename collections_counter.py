#!/usr/bin/env python3

from collections import Counter
X=int(input()) # Number of shoes in the store 
n=input() # String with shoes by size, which are available in the store
m=list(map(int, n.split()))# List with shoe sizes ready to be imported in the dictionary
dict=Counter(m) # {size: available amount}
# print(dict)
N=int(input()) # Number of customers
cashbox=0
for i in range(N):
    size=0
    price=0
    request=input().split()
    size=int(request[0])
    # print(size)
    price=int(request[1])
    # print(price)
    if size in dict.keys():
        amount=dict.get(size, 0)
        if amount!=0:
            dict[size]=amount-1
            cashbox+=price
print(str(cashbox))
