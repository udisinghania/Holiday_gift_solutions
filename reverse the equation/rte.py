n=int(input())
#print(ord('-'),ord('+'),ord('*'),ord('/'))
for i in range(n):
    s=input().rstrip()
    l=[]
    p=0
    o=0
    for j in range(1,len(s)):
        if ord(s[j])>=42 and ord(s[j])<=47:
            l.append(s[p:j])
            l.append(s[j])
            p=j+1
    l.append(s[p:])
    #print(l)
    f=[]
    for j in range (len(l)-1,-1,-1):
        f.append(l[j])
    f=''.join(f)        
    print(f)
