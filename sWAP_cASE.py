#!/usr/bin/env python3

def swap_case(s):
    while True:
        if len(s) > 1000:
            s = input()
            continue
        else:
            break
    d=''
    for i in s:
        if i.islower():
            d=d+i.upper()
        elif i.isupper():
            d=d+i.lower()
        else:
            d=d+i
    return d

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
