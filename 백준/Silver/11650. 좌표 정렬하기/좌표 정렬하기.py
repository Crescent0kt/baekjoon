import sys

N = int(sys.stdin.readline())

arr = []
for _ in range(N):
    x,y = map(int,sys.stdin.readline().split())
    arr.append((x,y))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    #1쪼갬
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    #2합침
    cur_left = 0
    cur_right = 0
    new_arr = []
    while cur_left <len(left) and cur_right< len(right):
        if left[cur_left][0] > right[cur_right][0] or (left[cur_left][0] == right[cur_right][0] and left[cur_left][1] > right[cur_right][1]):
            new_arr.append(right[cur_right])
            cur_right+= 1
        else:
            new_arr.append(left[cur_left])
            cur_left += 1
    else:
        while cur_left < len(left):
            new_arr.append(left[cur_left])
            cur_left += 1
        while cur_right< len(right):
            new_arr.append(right[cur_right])
            cur_right += 1

    return new_arr

new = merge_sort(arr)
for x,y in new:
    print(x,y)