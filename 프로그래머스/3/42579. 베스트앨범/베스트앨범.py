def solution(genres, plays):
    answer = []
    dict_genre = {}
    dict_count = {}
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        if genre in dict_genre:
            dict_genre[genre].append((-play,i))
            dict_count[genre] += play
        else:
            dict_genre[genre] = []
            dict_genre[genre].append((-play,i))
            dict_count[genre] = play
        
    genre_rank = []
    for key in dict_count.keys():
        genre_rank.append([dict_count[key],key])
    genre_rank.sort(reverse = True)
        
        
    for _,genre in genre_rank:
        music_list = dict_genre[genre]
        music_list.sort(key = lambda x:x[0])
        if len(music_list) == 1:
            answer.append(music_list[0][1])
        else:
            answer.append(music_list[0][1])
            answer.append(music_list[1][1])
    return answer