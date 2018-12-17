n=int(input())
for i in range (n):
    t=int(input())
    r=str(bin(t))
    r=r.split('b')
    l=list(r[1])
    #print(l)
    o=0
    for i in range (len(l)):
        if l.count('1')==2 and l[0]=='1' and l[-1]=='1':
            o=1
    print(o)        
            
