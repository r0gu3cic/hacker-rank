if __name__ == '__main__':
    while True:
        n = int(input())
        if 2 <= n <= 10:
            while True:
                arr = map(int, input().split())
                l = list(arr)
                if len(l) == n:
                    l.sort(reverse=True)
                    m = max(l)
                    while True:
                        if l[0]==m:
                            l.remove(m)
                            continue
                        else:
                            print(l[0])
                            break
                    break
                else:
                    continue
            break
        else:
            continue
