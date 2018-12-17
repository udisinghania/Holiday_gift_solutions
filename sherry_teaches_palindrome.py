t=int(input())
for i in range(t):
    n=input().rstrip()
    s=list(n)
    p=s
    if p==s[::-1]:
        if len(p)%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")