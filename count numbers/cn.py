from itertools import groupby
n=int(input())
for i in range (n):
    t=int(input())
    s=list(input().rstrip())
    #print(s)
    l=[]
    r=[]
    
    for q,w in groupby(s,lambda a: a>='0' and a<='9'):
        l.append(''.join(list(w)))
        r.append(q)
    print(r.count(True))
    
            
