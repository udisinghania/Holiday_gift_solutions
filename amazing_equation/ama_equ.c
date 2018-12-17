#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    long long int t;
    scanf("%lld",&t);
    for (long long int p=0 ; p<t; p++)
    {
        long long int a,b,x=10000,y=10000;
        scanf("%lld%lld",&a,&b);
        for (int i=1; i<b+1; i++)
        {
            for (int j=1; j<a+1; j++)
            {
                if (a*i==b*j && i<x && j<y )
                { x=i;
                  y=j;  
                break;
                }
            }
        }
        printf("%lld %lld\n",x,y);
    }
    
    return 0;
}
