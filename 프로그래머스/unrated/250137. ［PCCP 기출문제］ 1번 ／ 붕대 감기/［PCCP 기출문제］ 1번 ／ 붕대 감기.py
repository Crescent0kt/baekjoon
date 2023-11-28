#t초 동안 붕대를 감으면서 1초마다 x만큼 체력회복
#t초동안 붕대감는데 성공하면 y만큼 추가회복
# 최대체력 넘길 수 없음
# 공격당하면 취소, 당하는 순간에는 체력회복 x 
#기술이 취소 or 끝나면 붕대감기 재사용
#공격당하면 피해량만큼 체력감소
#현재 체력 0이하면 죽음
#끝까지 생존가능한지 여부
#bandage = [시전시간(t), 초당회복량(x), 추가회복량(y)]
#health = 최대체력
#attacks = [공격시간, 피해량]

def solution(bandage, health, attacks):
    past_time = 0
    t = bandage[0]
    x = bandage[1]
    y = bandage[2]
    health_now = health
    for time, damage in attacks:
        #이전시간까지 힐계산
        heal_time = time-past_time-1
        health_now += (heal_time//t) * (t*x + y) + (heal_time%t) * x
        if health<health_now:
            health_now = health
        #공격
        health_now -= damage
        if health_now <=0:
            return -1
        
        past_time = time
            
    return health_now