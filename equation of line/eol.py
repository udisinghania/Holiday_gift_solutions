n=int(input())
for i in range (n):
    s=input().rstrip().split(' ')
    a1,b1=int(s[0]),int(s[1])
    w=input().rstrip().split(' ')
    a2,b2=int(w[0]),int(w[1])
    l=[]
    l.append(str(b2-b1))
    l.append('x')
    if (a1-a2)<0:
        l.append(str(a1-a2))
    else:
        l.append('+')
        l.append(str(a1-a2))
    l.append('y')
    p=(a1*(b2-b1))-(b1*(a2-a1))
    l.append('=')
    l.append(str(p))
    t=''.join(l)
    print(t)
