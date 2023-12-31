"""
식은 0 - 9 + , - 로 이루어져 있음
괄호를 적절히 쳐서 식의 값을 최소로 만드는 프로그램을 작성하시오
처음과 마지막은 무조건 숫자이다.
연속해서 두 연산자가 나타나지 않고, 5자리 보다 많은 숫자는 없음, 수는 0으로 시작할 수 있고, 식의 길이는 50보다 작거나 같다.
"""

import sys

str = sys.stdin.readline().rstrip()
ans = 0
is_minus = False
tmp_str = ""

for s in str:
    if s == "+":

        if is_minus:
            ans -= int(tmp_str)
            tmp_str = ""
        else:
            ans += int(tmp_str)
            tmp_str = ""

    elif s == "-":

        if not is_minus:
            is_minus = True
            ans+= int(tmp_str)
            tmp_str = ""
        else:
            ans -= int(tmp_str)
            tmp_str = ""
    else:
        tmp_str += s
else:
    if is_minus:
        ans -= int(tmp_str)

    else:
        ans += int(tmp_str)


print(ans)