s=int(input())
for i in range (s):
    a=list(input().rstrip())
    b=list(input().rstrip())
    q=0
    w=0
    while q<len(a):
        d=a[q:]+a[0:q]
        #d.append(a[q:])
        #d.append(a[0:q])
        #print(d,b)
        if d==b:
            w=w+1
        q=q+1
    print(w)    
