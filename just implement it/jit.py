t=int(input())
for j in range (t):
    n=int(input())
    q=[]
    q.append('1')
    l=[]
    for i in range (1,n+1):
        w=q[0]
        l.append(str(w))
        l.append(' ')
        #print(w,end=' ')
        q=q[1:]
        q.append(str(w)+'0')
        q.append(str(w)+'1')
    #print(l,q)
    s=''.join(l)
    print(s)
