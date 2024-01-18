#!/usr/bin/env python3

def print_full_name(first, last):
    while True:
        if len(first)>=10:
            first=input()
        else:
            break
    while True:
        if len(last)>=10:
            last=input()
        else:
            break
    print('Hello '+first+' '+last+'! You just delved into python.')

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)