def sieve(a,b):
    prime = [True for i in range(b+1)]
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
    l=[]
    for p in range(a, b+1):
        if prime[p]:
            l.append(str(p))
    l=' '.join(l)
    print(l)
    #print('\n')    
 

n=int(input()) 
for i in range (n):
    s=input().rstrip().split(' ')
    a,b=int(s[0]),int(s[1])
    sieve(a,b)
    
