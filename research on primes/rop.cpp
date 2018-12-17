#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<bits/stdc++.h>
using namespace std;
 
void Sieve(int n)
{
    bool prime[n+1];
    memset(prime, true, sizeof(prime));
    for (int p=2; p*p<=n; p++)
    {
        // If prime[p] is not changed, then it is a prime
        if (prime[p] == true)
        {
            // Update all multiples of p
            for (int i=p*2; i<=n; i += p)
                prime[i] = false;
        }
    }
    int h=0;
    // Print all prime numbers
    for (int p=2; p<=n; p++)
    { if (prime[p])
          h=h+1;}
    cout<<h<<endl;       
}
 
// Driver Program to test above function
int main()
{
    
    int f=0,arr[100];
        while(cin>>arr[f])
    {
        Sieve(arr[f]);    
        f++;
    }
    
    
    return 0;
}
