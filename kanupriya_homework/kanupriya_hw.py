n = int(input())
l = list(map(int, input().split()))

sort = sorted(l)
rev = list(reversed(l))

d = {}
for i in range(n):
    if sort[i] not in d:
        d[sort[i]] = i   # {1:0 , 2:1 , 3:2 , 5:3 }

asc = 0
i = 0
while i < n:
    if sort[i] == l[i]:
        i += 1
        continue
    asc += 1
    l[d[l[i]]], l[i] = l[i], l[d[l[i]]]
    d[sort[i]] += 1

d = {}
for i in range(n):
    if sort[i] not in d:
        d[sort[i]] = i

desc = 0
i = 0
while i < n:
    if sort[i] == rev[i]:
        i += 1
        continue
    desc += 1
    rev[d[rev[i]]], rev[i] = rev[i], rev[d[rev[i]]]
    d[sort[i]] += 1

print(min(asc, desc))
