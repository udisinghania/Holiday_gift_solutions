#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
/*def fun(arr):
    re=0
    for i in range (len(arr)):
        re=re^arr[i]
    return re;
n=int(input())
s=input().rstrip().split(' ')
a=[int(i) for i in s]
print(fun(a))*/
int fun(int arr[], int n)
{
    int re=0;
    for (int i=0; i<(2*n)+1; i++)
    {
        re=re^arr[i];
    }
    return re;
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n;
    cin>>n;
    int a[(2*n)+1];
    for (int i=0; i<(2*n)+1; i++)
    {
        cin>>a[i];
    }
    int h=0;
    h=fun(a,n);
    cout<<h;
        return 0;
}
