n=int(input())
for i in range (n):
    a=input().rstrip().split(' ')
    j,k=int(a[0]),int(a[1])
    s=input().rstrip().split(' ')
    s=[list(str(bin(int(h)))[2:]).count('1') for h in s]
    t=sorted(s)
    #print(t)
    p=0
    for y in range (j-k,j):
        p=p+t[y]
        #print(p)
    print(p)    
