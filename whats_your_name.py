def print_full_name(a, b):
    while True:
        if len(a)>=10:
            a=input()
        else:
            break
    while True:
        if len(b)>=10:
            b=input()
        else:
            break
    

    print('Hello '+a+' '+b+'! You just delved into python.')

