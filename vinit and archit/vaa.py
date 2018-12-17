n=int(input())
for i in range (n):
    s=input().rstrip().split(' ')
    d=[]
    for j in range (len(s)):
        if d.count(s[j])<1:
            d.append(s[j])
    f=[]
    for j in range (len(d)):
        f.append(s.count(d[j]))
    r=max(f)
    t=f.index(r)
    print(d[t],r)
    
