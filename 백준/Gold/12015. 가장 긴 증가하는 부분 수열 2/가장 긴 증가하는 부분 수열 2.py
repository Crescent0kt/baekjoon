def bisect_func(target, start, end):
    while start<end:
        mid = (start+end)//2
        if target > lst[mid]:
            start = mid+1
        else:
            end = mid

    return end

N = int(input())
sequence = list(map(int,input().split()))

lst = [sequence[0]]
for i in range(1, N):
    if lst[-1] < sequence[i]:
        lst.append(sequence[i])
    else:
        p = bisect_func(sequence[i],0,len(lst))
        lst[p] = sequence[i]

print(len(lst))

