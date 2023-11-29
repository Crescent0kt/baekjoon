def solution(n, k, cmd):
    answer = ''
    deleted = []
    up = [x-1 for x in range(n + 2)]
    down = [x+1 for x in range(n + 1)]
    
    k += 1
    
    for cmd_i in cmd:
        c = cmd_i.split(" ")
        if c[0] == "U":
            for _ in range(int(c[1])):
                k = up[k]
                
        elif c[0] == "D":
            for _ in range(int(c[1])):
                k = down[k]
        elif c[0] == "C":
            #1 지우기
            deleted.append(k)
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            k = up[k] if n < down[k] else down[k]
            
        elif c[0] == "Z":
            restore = deleted.pop()
            up[down[restore]] = restore
            down[up[restore]] = restore
    
    answer = ["O"] * n
    for i in deleted:
        answer[i-1] = "X"
    return ''.join(answer)