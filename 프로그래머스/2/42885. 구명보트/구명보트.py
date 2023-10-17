def solution(people, limit):
    answer = 0
    num_people = len(people)
    people.sort()
    cursor_l = -1
    cursor_r = len(people)-1
    
    while cursor_l != cursor_r:
        cursor_l += 1
        answer += 1
        a = people[cursor_l]
        while cursor_l != cursor_r:
            if people[cursor_r] + a <= limit:
                cursor_r -= 1
                num_people -= 1
                break
            cursor_r -= 1
        num_people -= 1
        
    answer += num_people
    return answer