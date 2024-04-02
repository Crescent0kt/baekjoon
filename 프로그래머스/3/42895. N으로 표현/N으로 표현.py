def solution(N, number):
    if number == N:
        return 1
    num_list = []
    
    for count in range(1,9):
        num_set = set()
        num_set.add(int(str(N)*count))
        
        for i in range(count - 1):
            for num1 in num_list[i]:
                for num2 in num_list[-i-1]:
                    num_set.add(num1 + num2)
                    num_set.add(num1 - num2)
                    num_set.add(num1 * num2)
                    if num2 != 0:
                        num_set.add(num1 / num2)
        if number in num_set:
            return count
        num_list.append(num_set)
    return -1