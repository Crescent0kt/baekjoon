import sys

str = sys.stdin.readline().rstrip()

num = 0
ans = 0
if "-" in str:
    plus, minus = str.split("-",1)[0], str.split("-",1)[1]
    p = sum(map(int,plus.split("+")))

    minus = minus.replace("-", "+")
    m = sum(map(int,minus.split("+")))
else:
    plus, minus = str, ""
    p = sum(map(int,plus.split("+")))
    m = 0

print(p-m)