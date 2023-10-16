def solution(quiz):
    answer = []
    for quiz_element in quiz:
        x, oper, y, equal, z = quiz_element.split()
        
        if oper == "+":
            if int(x) + int(y) == int(z):
                answer.append("O")
            else: answer.append("X")
        else: 
            if int(x) - int(y) == int(z):
                answer.append("O")
            else: answer.append("X")
    return answer