n=int(input())
for i in range (n):
    s=list(input().rstrip())
    #print(s)
    if ord(s[0])>=65 and ord(s[0])<=90:
        for j in range (1,len(s),2):
            if ord(s[j])>=65 and ord(s[j])<=90:
                s[j]=chr(ord(s[j])+32)
        for j in range (2,len(s),2):
            if ord(s[j])>=97 and ord(s[j])<=122:
                s[j]=chr(ord(s[j])-32)
                
    elif ord(s[0])>=97 and ord(s[0])<=122:
        for j in range (2,len(s),2):
            if ord(s[j])>=65 and ord(s[j])<=90:
                s[j]=chr(ord(s[j])+32)
        for j in range (1,len(s),2):
            if ord(s[j])>=97 and ord(s[j])<=122:
                s[j]=chr(ord(s[j])-32)
                
    s=''.join(s)
    print(s)
