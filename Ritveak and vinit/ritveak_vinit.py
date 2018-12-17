n=int(input())
s=input().rstrip().split(' ')
l=[int(i) for i in s]
t=int(input())
l.sort()
r=1000
for i in range(len(l)):
    if l.count(l[i])==t and r>l[i]:
        r=l[i]
print(r)        
