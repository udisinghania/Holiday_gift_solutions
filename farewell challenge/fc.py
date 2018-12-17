n=int(input())
for i in range (n):
    s=input().rstrip().split(' ')
    a,b=list(s[0]),list(s[1])
    a.sort()
    b.sort()
    if a==b:
        print('FAREWELL')
    else:
        print("NOT NOW")
