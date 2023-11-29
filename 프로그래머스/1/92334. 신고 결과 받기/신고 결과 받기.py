def solution(id_list, report, k):
    answer = []
    #리포트 셋으로 변경 -> 중복 제거
    report = list(set(report))
    report_dict = {} #신고당한 유저 - 신고유저
    user_dict = {} #유저 - 받을거
    
    for log in report:
        fr, to = log.split(" ") #fr - 내가 to - 너를 신고
        if to in report_dict:
            report_dict[to].append(fr)
        else:
            report_dict[to] = []
            report_dict[to].append(fr)
    
    for u_id in id_list:
        if u_id in report_dict and len(report_dict[u_id])>=k:
            for reporter_id in report_dict[u_id]:
                if reporter_id in user_dict:
                    user_dict[reporter_id] +=1
                else: user_dict[reporter_id] = 1
                    
    for u_id in id_list:
        if u_id in user_dict:
            answer.append(user_dict[u_id])
        else:
            answer.append(0)
    return answer