t=int(input())
for i in range (t):
    n=int(input())
    s=list(input().rstrip().split(' '))
    n1=''.join(s)
    n1=int(n1)
    m=int(input())
    s1=list(input().rstrip().split(' '))
    n2=''.join(s1)
    n2=int(n2)
    print(n1+n2)
