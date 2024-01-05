import sys
import math
T = int(sys.stdin.readline())

for _ in range(T):
    #두 중심점 사이 거리 구해서
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    #비교

    #둘이 같은 중심인데, r 겹친다, 안겹친다
    if dist == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)

    else:
        #두 중심의 거리 == r1 + r2 => 외접
        #두 중심의 거리 == abs(r1 - r2) => 내접
        if dist == r1+r2 or dist == abs(r1-r2):
            print(1)
        #두 점 겹침 -> 내접 외접 사이
        elif abs(r1-r2) < dist < r1+r2:
            print(2)
        #안겹침
        else:
            print(0)