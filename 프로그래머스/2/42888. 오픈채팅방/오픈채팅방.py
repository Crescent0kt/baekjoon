def solution(record):
    answer = []
    user = {}
    user_log = []
    for log in record:
        u_log = log.split(" ")
        user_log.append([u_log[0],u_log[1]])
        if len(u_log) != 2:
            user[u_log[1]] = u_log[2]
        
    for log in user_log:
        if log[0] == "Enter":
            chat = user[log[1]] + "님이 들어왔습니다."
            answer.append(chat)
        elif log[0] == "Leave":
            chat = user[log[1]] + "님이 나갔습니다."
            answer.append(chat)            
    return answer