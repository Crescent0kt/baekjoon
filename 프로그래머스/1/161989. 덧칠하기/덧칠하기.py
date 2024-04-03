def solution(n, m, section):
    answer = 0
    section.sort()
    pointer = 0
    for sec in section:
        if pointer < sec:
            answer += 1
            pointer = sec+m - 1
        else:
            continue

    return answer