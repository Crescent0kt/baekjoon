#입차 후 출차 내역이 없으면 23:59 출차로 간주
#누적 시간이 기본 시간을 초과하면 기본요금에 더해서 초과한 시간에 대해 단위 시간마다 단위 요금 청구
#초과한 시간이 단위 시간으로 나누어 떨어지지 않으면 올림
# 요금표 1. 기본시간 2 기본요금 3 단위시간 4 단위 요금
# 차량 : 시각, 차량번호, 내역이 공백으로 구분

#차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 리턴하도록
from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    d_time = fees[0]
    d_fee = fees[1]
    u_time = fees[2]
    u_fee = fees[3]
    
    dict_rec = defaultdict(int)
    dict_time = defaultdict(int)
    key_set = set()
    for record in records:
        t, n, h = record.split()
        hour, minute = map(int,t.split(":"))
        time = int(hour*60) + int(minute)
        if h == "IN":
            dict_rec[n] = time
            key_set.add(n) 
        else:
            cal_time =  time - dict_rec[n]
            dict_rec.pop(n)
            dict_time[n] += cal_time

    
    for key in sorted(key_set):
        if key in dict_rec:
            time = 23*60+59
            cal_time =  time - dict_rec[key]
            dict_time[key] += cal_time
        if dict_time[key] <= d_time:
            answer.append(d_fee)
        else:
            answer.append(d_fee + math.ceil((dict_time[key]-d_time)/u_time) * u_fee)
    return answer