n=int(input())
for i in range (n):
    #l=[]
    #s=[]
    t=int(input())
    p=list(str(t))
    r=0
    for j in range(len(p)):
        if p.count(p[j])>=r:
            r=p.count(p[j])
            t=int(p[j])
    print(t)        
            
            
            
