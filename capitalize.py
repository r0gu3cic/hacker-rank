#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    lista=s.split(' ')
    stampa=''
    for i in lista:
        if i=='':
            stampa+=' '
        else:
            uvecano=i[0].upper()
            ukloni=i[1:]
            dodaj=uvecano+ukloni
            stampa+=dodaj+' '
    return stampa

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
