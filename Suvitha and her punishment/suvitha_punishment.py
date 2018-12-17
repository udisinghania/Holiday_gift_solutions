n=int(input())
for i in range (n):
    p=0
    s=input().rstrip()
    for j in range(len(s)):
        for t in range (j+1,len(s)):
            if s[t]==s[j]:
                p=p+1
                break;
    if p==0:
        print(1)
    else:
        print(0)
