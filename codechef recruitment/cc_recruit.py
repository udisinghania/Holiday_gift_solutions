t=int(input())
for i in range (t):
    n=int(input())
    s=input()
    #s.lower()
    #print(s)
    l=[]
    for j in range (n):
        if ord(s[j])>=65 and ord(s[j])<=90:
            print(s[j])
            l.append(chr(ord(s[j])+32))
        else:
            l.append(s[j])    
    
   # print(l)
    p='0'
    for j in range (n):
        if l.count(l[j])==1:
            p=l[j]
            break;
    if p!='0':
        print(p)        
    else:
        print(-1)
