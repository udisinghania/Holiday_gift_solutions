t=int(input())
for i in range (t):
    n=int(input())
    s=input().rstrip().split(' ')
    l=[int(j) for j in s]
    p=[]
    k=0
    for j in range(len(l)):
        if l.count(l[j])>=4 and p.count(l[j])<1:
            p.append(l[j])
            if l[j]>=max(p):
                k=int(l.count(l[j])//4)
    if p==[]:
        print(-1)
    else:
        print(max(p)**2,k)
