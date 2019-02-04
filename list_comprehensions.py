if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    i=0
    j=0
    k=0
    ll=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                nl=[i,j,k]
                if i+j+k!=n:
                    ll.append(nl)

                k+=1
            j+=1
        i+=1
    print(ll)
