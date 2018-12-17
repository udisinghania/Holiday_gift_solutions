def result(e):
    t=1
    w=0
    while t%e!=0:
        t=t*(w+1)
        w+=1
        #print(t,w)
    return w;
n=int(input())
print(result(n))
