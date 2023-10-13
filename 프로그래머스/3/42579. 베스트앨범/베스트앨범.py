
def solution(genres, plays):
    answer = []
    dict = {}
    #song = 고유번호 ->[재생횟수, 장르]
    song = []
    for i, genre in enumerate(genres):
        if genre in dict:
            dict[genre] +=plays[i]
        else:
            dict[genre] = plays[i]
        song.append([plays[i],genre])

    #sort_dict = 아이템들을 play값으로 내림차순으로 정렬, 이게 장르 순서 
    sort_dict = sorted(dict.items(),key=lambda x:x[1],reverse=True)
    
    #제일 큰 sort_dict부터 끝까지 => 모든장르에서
    for i in range(len(sort_dict)):
        tmparr = []
        
        #j == 번호 element == [plays[i],genre]
        #현재 song의 장르가 지금 보는 장르와 같으면
        #재생수, 고유번호 배열에 넣음
        for j,element in enumerate(song):
            if element[1] == sort_dict[i][0]:
                tmparr.append([song[j][0],j])
                
        if len(tmparr) <= 1:
            answer.append(tmparr.pop()[1])
        else:
            tmparr.sort(key = lambda x: (x[0], -x[1]))
            answer.append(tmparr.pop()[1])
            answer.append(tmparr.pop()[1])
    return answer