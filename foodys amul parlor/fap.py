n=int(input())
if n>=1 and n<=50:
    for i in range(n):
        t=int(input())
        r=int(input())
        if t>=2 and t<=10000 and r>=2 and r<=10000:
            s=input().rstrip().split(' ')
            e=[int(j) for j in s]
            l=sorted(e)
            
            o=0
            p=0
            for j in range (r):
                for k in range (j+1,r):
                    if l[j]+l[k]==t:
                        o=e.index(l[j])
                        e[o]=0
                        #if e.index(l[k])!=o:
                        p=e.index(l[k])
                        break
                    else:
                        continue

            print(min(o+1,p+1),max(o+1,p+1))            
