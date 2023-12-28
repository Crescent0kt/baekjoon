import sys
import heapq
INF = int(1e9)
N,K = map(int,sys.stdin.readline().split())
if K<=N:
    print(abs(K-N))
    exit()
visited = [INF] * (K+1)
#시간, 위치
q = [(0, N)]
ans = INF
while q:

    time, pos = heapq.heappop(q)

    if pos == K:
        ans = min(ans,time)
        break

    #이미 본애들, 볼 가치 없는 애들
    if visited[pos] < time:
        continue

    # -1 이동
    if pos-1 >= 0 and visited[pos-1] > time+1:
        visited[pos-1] = time+1
        heapq.heappush(q, (time+1, pos-1))
    # +1 이동
    if pos+1 <= K and visited[pos + 1] > time + 1:
        visited[pos + 1] = time + 1
        heapq.heappush(q, (time + 1, pos + 1))

    #배수 이동
    pos = pos *2
    while pos <= K:
        if visited[pos] > time:
            visited[pos] = time
            heapq.heappush(q,(time, pos))
            pos = pos * 2
        else:
            break
    else:
        ans = min(ans,time+ pos-K)
print(ans)