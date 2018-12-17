l=[]
f=[]
n=int(input())
for i in range (n):
    s=input().rstrip().split(' ')
    a,b=int(s[0]),int(s[1])
    l.append(a)
    f.append(b)
prime = [True for i in range(max(f)+1)]
p = 2
prime[1]=False
while (p * p <= b+1):
    # If prime[p] is not changed, then it is a prime
    if (prime[p] == True):  
        # Update all multiples of p
        for i in range(p*2, b+1, p):
            prime[i] = False
    p += 1 
# Print all prime numbers
for i in range (n):
    r=0
    for j in range (l[i],f[i]+1):
        e=list(str(j))
        w=[int(d) for d in e]
        q=[int(d)**2 for d in e]
        if prime[sum(w)]==True and prime[sum(q)]==True:
            r=r+1
    print(r)
