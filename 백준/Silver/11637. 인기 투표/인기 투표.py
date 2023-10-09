import sys

T = int(sys.stdin.readline())

for i in range(T):

    n = int(sys.stdin.readline())
    count = 0
    winner = 0
    who = 0
    for i in range(n):

        p = int(sys.stdin.readline())
        count += p
        if winner < p:
            winner = p
            who = i+1
        elif winner == p:
            who = -1
    
    if who == -1: print("no winner")
    elif count/2 < winner: print("majority winner", who)
    else : print("minority winner", who)
