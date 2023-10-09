import sys
from itertools import combinations

N,K = map(int,sys.stdin.readline().split())

def factorial(n):
    a = 1
    for i in range(1,n+1):
        a *= i
    return a

print(factorial(N)//(factorial(K)*factorial(N-K)))