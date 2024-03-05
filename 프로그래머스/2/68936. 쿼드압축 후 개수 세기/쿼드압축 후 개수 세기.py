def solution(arr):
    answer = []
    global zero
    zero =0
    global one
    one = 0
    def func(arr,x,y,n):
        global zero
        global one
        if arr[y][x] == 0:
            for i in range(y,y+n):
                check = False
                for j in range(x, x+n):
                    if arr[i][j] != 0:
                        check = True
                        break
                if check:
                    func(arr,x,y,n//2)
                    func(arr,x+n//2,y,n//2)
                    func(arr,x,y+n//2,n//2)
                    func(arr,x+n//2,y+n//2,n//2)
                    break
            else:
                zero += 1   
        else:   
            for i in range(y,y+n):
                check = False
                for j in range(x, x+n):
                    if arr[i][j] != 1:
                        check = True
                        break
                if check:
                    func(arr,x,y,n//2)
                    func(arr,x+n//2,y,n//2)
                    func(arr,x,y+n//2,n//2)
                    func(arr,x+n//2,y+n//2,n//2)
                    break
            else:
                one += 1
    func(arr,0,0,len(arr))
    answer.append(zero)
    answer.append(one)
    return answer