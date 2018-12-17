n=int(input())
for i in range (n):
    s=input().rstrip().split(' ')
    r=0
    l=[]
    t=0
    while r!=len(s[0])+len(s[1]):
        if len(s[0])>t and len(s[1])>t:
            l.append(s[0][t])
            l.append(s[1][t])
            t=t+1
            r=r+2
        elif len(s[0])>t and len(s[1])<=t:
            l.append(s[0][t])
            t=t+1
            r=r+1
        elif len(s[0])<=t and len(s[1])>t:
            l.append(s[1][t])
            t=t+1
            r=r+1
    l=''.join(l)
    print(l)        
            
