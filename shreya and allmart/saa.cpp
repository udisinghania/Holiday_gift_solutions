#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <bits/stdc++.h>
using namespace std;
 
void Sieve(long long int h,long long int n,long long int a[],long long int y)
{
    bool prime[n+1];
    memset(prime, true, sizeof(prime));
    for(long long int j=0; j<y; j++)
    {   
        for (long long int i=a[j]; i<=n; i += a[j])
            prime[i] = false;
    }
    
    long long int c=0;
    for (long long int p=h; p<=n; p++)
       if (prime[p]==false)
          c+=1;
    cout<<c<<endl;
}
 
int main()
{
    long long int n,h,y;
    cin>>y;
    long long int a[y];
    for(long long int i=0; i<y; i++)
    {cin>>a[i];}
    long long int r;
    cin>>r;
    for (long long int i=0; i<r; i++)
    {
        cin>>h>>n;
        Sieve(h,n,a,y);
    }
    return 0;
}
