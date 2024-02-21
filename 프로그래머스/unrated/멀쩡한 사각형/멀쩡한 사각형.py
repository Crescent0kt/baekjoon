import math

def solution(w, h):
    gcd = math.gcd(w, h)
    a = w / gcd
    b = h / gcd
    cut_in_small_rectangle = a + b - 1
    total_cut = cut_in_small_rectangle * gcd
    usable_squares = (w * h) - total_cut
    return usable_squares