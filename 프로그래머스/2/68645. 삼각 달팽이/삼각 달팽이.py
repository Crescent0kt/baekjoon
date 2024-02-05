def solution(n):
    answer = [[0] * n for _ in range(n)]
    x, y, count = -1, 0, 1

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            answer[x][y] = count
            count += 1

    result = [num for sublist in answer for num in sublist if num != 0]
    return result
