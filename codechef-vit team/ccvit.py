s=input().rstrip().split(' ')
a,b=int(s[0]),int(s[1])
p=[]
for i in range(a):
    s=list(input().rstrip())
    l=[int(j)  for j in range(len(s)) if int(s[j])==1  ]
    p.append(l)
#print(p)

#print(set(p[0])|set(p[1]))
m=0
t=0
for i in range (a):
    for j in range (i+1,a):
        if len(set(p[i])|set(p[j]))>=m:
            m=len(set(p[i])|set(p[j]))
            y=set(p[i])|set(p[j])

for i in range (a):
    for j in range (i+1,a):
        if len(set(p[i])|set(p[j]))==m:
            t=t+1
#print(y)
p=list(y)

o=0
for i in p:
    if i>=0:
        o+=1
print(o)
print(t)            
