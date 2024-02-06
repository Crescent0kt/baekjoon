def solution(order):
    answer = 0
    count = 1
    stack = []

    for o in order:
        while count <= o:
            stack.append(count)
            count += 1

        if stack and stack[-1] == o:
            stack.pop()
            answer += 1
        else:
            break

    return answer
