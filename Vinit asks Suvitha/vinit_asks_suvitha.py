n=int(input())
l=[]
l.append(0)
for i in range(n):
    t=int(input())
    for j in range (100,4,-5):
        e=int(j//25)+int(j//5)
        if t==e:
            print(j)
