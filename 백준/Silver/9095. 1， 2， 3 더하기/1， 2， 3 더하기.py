import sys

T = int(sys.stdin.readline())
answer_set = set()
def find_n(n,arr):
    for i in range(n-1):
        if arr[i]+arr[i+1] <=3:
            new_arr = arr[:i] + [arr[i]+arr[i+1]] + arr[i+2:]
            new_tuple = tuple(new_arr)
            if new_tuple not in answer_set:
                answer_set.add(new_tuple)
                find_n(n-1, new_arr)


for _ in range(T):
    n = int(sys.stdin.readline())
    answer_set = set()
    find_n(n,[1] * n)
    print(len(answer_set)+1)
