def solution(book_time):
    answer = 0
    arr = []
    book_time.sort(key=lambda x: x[0])
    for start, end in book_time:
        start_hour, start_min = map(int,start.split(":"))
        start_time = start_hour * 60 + start_min
        end_hour, end_min = map(int,end.split(":"))
        end_time = end_hour * 60 + end_min
        for i in range(len(arr)):
            if arr[i] <= start_time:
                arr[i] = end_time + 10
                break
        else:
            arr.append(end_time + 10)

    return len(arr)