import math

def solution(w, h):
    gcd = math.gcd(w, h)
    a = w / gcd
    b = h / gcd
    #최대 공약수에서의 가로 이동 수, 세로 이동 수, 중복되는 지점 하나 빼주기
    #2 ,3에서는 가로2번, 세로 3번 이동이지만 중복 지점 -1
    cut_in_small_rectangle = a + b - 1
    total_cut = cut_in_small_rectangle * gcd
    usable_squares = (w * h) - total_cut
    return usable_squares