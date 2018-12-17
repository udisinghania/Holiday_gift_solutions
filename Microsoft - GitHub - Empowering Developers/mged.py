n=int(input())
for i in range (n):
    t=int(input())
    l=[]
    p=[]
    s=input().rstrip().split(' ')
    for j in range (t):
        if l.count(s[j])<1:
            p.append('Verified')
            p.append(' ')
        else:
            r=l.count(s[j])
            #print(r)
            p.append(s[j]+str(r))
            p.append(' ')
        l.append(s[j])    
    y=''.join(p)
    print(y)        
