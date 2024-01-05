import sys

while True:
    str = sys.stdin.readline()
    if str[0] == ".":
        break

    stack = []
    for s in str:
        if s == "(" or s == "[":
            stack.append(s)

        elif s == ")":
            if not stack or stack[-1] != "(":
                print("no")
                break
            else:
                stack.pop()

        elif s == "]":
            if not stack or stack[-1] != "[":
                print("no")
                break
            else:
                stack.pop()

        elif s == ".":
            if not stack:
                print("yes")
            else:
                print("no")
            break
