s=input().rstrip().split(' ')
a=[int(i) for i in s]
w=0
w=w+a[-1]
#print(w)
w=w+min(a[0],a[2])
#print(w)
r=min(a[0],a[2])
a[0]=a[0]-r
a[2]=a[2]-r
w=w+a[2]
#print(w,a[2])
if (a[1]%2==0):
    w=w+int(a[1]/2)
    if (a[0]%4)==0:
        w=w+int((a[0])/4)
        #print(w)
    else :
        w=w+int((a[0])/4)+1
        #print(w)
else:
    w=w+int((a[1]-1)/2)
    if (a[0]+2)%4==0:
        w=w+int((a[0]+2)/4)
        #print(w)
    else:
        w=w+int((a[0]+2)/4)+1
        #print(w)
print(w)
