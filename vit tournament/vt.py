def fun(n,h):
    if h==2:
        l=[1,0]
        print(len(l))
    elif h==3:  
        no=n #number you want to change
        p=h  #in the terms of how many changes do you want. 
        l=[]
        t=0
        g=[]
        while t<=n:
            m=[]
            no=n
            no=no-t
            #print(no,t)
            #k.append(t)
            #print(k)
            y=0
            p=max(no,t)
            while y<=p and (no>=0 and t>=0):
                k=[]
                k.append(t)
                k.append(y)
                j=n-t-y
                k.append(n-t-y)
                if k.count(0)<2 and (j>=0):
                    m.append(k)
                y+=1
            #print(m)
            #print(len(m))
            t+=1
            if len(m)!=0:
                l.append(m)
                g.append(len(m))
        print(sum(g))


t=int(input()) #no. of testcases
for i in range (t):
    n=int(input()) #len of array
    s=input().rstrip().split(' ')
    l=[int(j) for j in s] #numbers in array
    r=n;
    p=0
    for j in range (n):
        if l[j]>=0:
            r=r-l[j];
            p=p+l[j]
    if r<=0:
        if n==2:
            if l.count(1)==2:
                print(0)
            else:
                print(1)
        else:
            print(1)
    else:
        p=int(n*(n-1)/2)-p #no. of elements 
        r=l.count(-1)
        #print(p,r)
        s=fun(p,r)
        #print(s)
