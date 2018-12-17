n=int(input())
for i in range (n):
    s=input().rstrip()
    p=len(s)
    e=0
    s=s.split('.')
    f=['a','e','i','u','o','A','I','O','E','U']
    for j in range(len(s[1])):
        if s[1][j] not in f:
            e=e+1
            #print(s[1][j])
    print(str(e+4)+"/"+str(p))        
