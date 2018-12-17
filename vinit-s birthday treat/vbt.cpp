#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    long long int n;
    cin>>n;
    for (long long int i=0; i<n; i++ )
    {
        long long int s;
        cin>>s;
        cout<<s*(s-1)/2<<endl;
    }
    return 0;
}
