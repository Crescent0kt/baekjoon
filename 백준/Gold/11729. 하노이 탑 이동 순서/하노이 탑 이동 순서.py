arr1 =[]
arr2 =[]

def Hanoi(a,b,c,N):
    if N ==0:
        return
    Hanoi(a,c,b,N-1)
    arr1.append(a)
    arr2.append(c)
    Hanoi(b,a,c,N-1)

Hanoi(1,2,3,int(input()))
print(len(arr1))
for i in range(len(arr1)):
    print(arr1[i],arr2[i])