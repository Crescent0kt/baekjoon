import sys

while True:
    n,m,k = map(int,sys.stdin.readline().split())
    if n == m == k == 0:
        break
    #시작 배열 선언
    arr = [True] * n
    #기본 전략 k 번 반복 -> 해당하는 위치에 배열 체크
    cursor = -1
    #정답 가리기 전 지우기
    for _ in range(k-1):
        #m번 건너뛰기
        count = m
        while count>0:
            cursor = (cursor +1) % n
            count -= 1
            while not arr[cursor]:
                cursor = (cursor+1)%n

        arr[cursor] = False
    #정답 도출
    else:
        count = m
        while count > 0:
            cursor = (cursor + 1) % n
            count -= 1
            while not arr[cursor]:
                cursor = (cursor + 1) % n
        #0 - 19 to 1 - 20
        print(cursor+1)