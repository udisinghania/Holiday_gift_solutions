#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <bits/stdc++.h>
using namespace std;

/*

for i in range (n):
    r=0
    for j in range (l[i],f[i]+1):
        e=list(str(j))
        w=[int(d) for d in e]
        q=[int(d)**2 for d in e]
        if prime[sum(w)]==True and prime[sum(q)]==True:
            r=r+1
    print(r)
*/
int prite(long long int n)
{
   long long int r=0;
    while (n>0)
    {
        r=n%10+r;
        n=n/10;
    }
    return r;
}

int sprite(long long int n)
{
   long long int r=0;
    while (n>0)
    {
        r=((n%10)*(n%10))+r;
        n=n/10;
    }
    return r;
}
int prit(long long int n)
{
   long long int r=0,e=0;
    while (n>0)
    {
        r=((n%10)*(n%10))+r;
        n=n/10;
        e+=1;
    }
    return e;
}
int main() 
{
    long long int n;
    cin>>n;
    long long int a[n],b[n],s=0,l=0;
    for (long long int i=0; i<n; i++)
    {
        cin>>a[i]>>b[i];
        if (b[i]>l) 
        {
            l=b[i];
            l=pow(9,prit(l));
        }
    }
    bool prime[l];
    memset(prime, true, sizeof(prime));
    prime[1]=false;
    for (long long int p=2; p*p<=l; p++)
    {
        if (prime[p] == true)
        {
            for (long long int i=p*2; i<=l; i += p)
                prime[i] = false;
        }
    }
    for (long long int t=0; t<n; t++)
    {
        long long int y=0;
        for (long long int h=a[t]; h<=b[t]; h++)
        {
            long long int r=prite(h);
            long long int g=sprite(h);
            
            if (prime[r]==true && prime[g]==true)
            {   //cout<<r<<' '<<g<<endl;
                y=y+1;
            }
        }
        cout<<y<<endl;
    }
    
    return 0;
}
