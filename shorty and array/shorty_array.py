def fun(arr):
    re=0
    for i in range (len(arr)):
        re=re^arr[i]
    return re;
n=int(input())
s=input().rstrip().split(' ')
a=[int(i) for i in s]
print(fun(a))
