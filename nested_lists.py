from operator import itemgetter
if __name__ == '__main__':
    whole_set=[]
    n=int(input())
    for _ in range(n):
        name = input()
        score = float(input())
        new_set=[name,score]
        whole_set.append(new_set)
    sort_by_grade=sorted(whole_set, key=itemgetter(1), reverse=True)
    first=[]
    lowest_grade=sort_by_grade[n-1]
    for i in sort_by_grade:
        if i[1]==lowest_grade[1]:
            pass
        else:
            first.append(i)
    second=[]
    lowest_grade=first[len(first)-1]
    for i in first:
        if i[1]==lowest_grade[1]:
            second.append(i)
        else:
            pass
    sort_by_name=sorted(second, key=itemgetter(0))
    for i in  sort_by_name:
        print(i[0])
        
