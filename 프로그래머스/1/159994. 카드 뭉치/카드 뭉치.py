from collections import deque
def solution(cards1, cards2, goal):
    answer = ''
    cards_one = deque(cards1)
    cards_two = deque(cards2)
    
    for word in goal:
        if len(cards_one) != 0 and word == cards_one[0]:
            cards_one.popleft()
        elif len(cards_two)!=0 and word == cards_two[0]:
            cards_two.popleft()
        else:
            return "No"
    else: return "Yes"