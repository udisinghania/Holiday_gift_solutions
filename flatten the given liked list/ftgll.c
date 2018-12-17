#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
void merge(int arr[], int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 =  r - m;
    int L[n1], R[n2];
 
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1+ j];
 
    /* Merge the temp arrays back into arr[l..r]*/
    i = 0; // Initial index of first subarray
    j = 0; // Initial index of second subarray
    k = l; // Initial index of merged subarray
    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            arr[k] = L[i];
            i++;
        }
        else
        {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
 
    while (i < n1)
    {
        arr[k] = L[i];
        i++;
        k++;
    }
 
    while (j < n2)
    {
        arr[k] = R[j];
        j++;
        k++;
    }
}
 
void mergeSort(int arr[], int l, int r)
{
    if (l < r)
    {
        int m = l+(r-l)/2;
 
        mergeSort(arr, l, m);
        mergeSort(arr, m+1, r);
 
        merge(arr, l, m, r);
    }
}
 
void printArray(int A[], int size)
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", A[i]);
    printf("\n");
}
 
int main() {

    int n;
    scanf("%d",&n);//cin>>n;
    for (int i=0; i<n; i++)
    {
        int m;
        scanf("%d",&m);//cin>>m;
        int a[m],s=0;
        for (int j=0; j<m; j++)
        {   scanf("%d",&a[j]);//cin>>a[j];
            s=s+a[j];
        }
        int b[s];
        for (int j=0; j<s; j++)
        {
            scanf("%d",&b[j]);//cin>>b[j];
        }
        mergeSort(b,0,s-1);
        printArray(b,s);
    }
    return 0;
}
