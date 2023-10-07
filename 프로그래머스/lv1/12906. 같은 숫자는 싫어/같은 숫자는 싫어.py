def solution(arr):
    answer = []
    a = arr[0]
    answer.append(a)
    for i in range(1,len(arr)):
        if a != arr[i]:
            answer.append(arr[i])
            a = arr[i]
    return answer