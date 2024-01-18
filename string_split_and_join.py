#!/usr/bin/env python3

def split_and_join(line):
    a=line
    b=b=a.split()
    separator='-'
    result=separator.join(b)
    return result
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
