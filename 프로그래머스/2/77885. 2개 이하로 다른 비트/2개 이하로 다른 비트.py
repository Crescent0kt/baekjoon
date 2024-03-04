def func(num):
    numBin = list(bin(num)[2:])
    for i in range(len(numBin)-1, -1, -1):
        if numBin[i] == "0":
            numBin[i] = "1"
            if i != len(numBin)-1:
                numBin[i+1] = "0"
            break
    else:
        numBin = ["1"] + numBin
        numBin[1] = "0"
    return int(''.join(numBin), 2)
    
def solution(numbers):
    answer = []
    for num in numbers:
        answer.append(func(num))
    return answer