import sys

T = int(sys.stdin.readline())


def func1(str, path, ans):
    if not str:
        ans.append(path)

    for i in range(len(str)):
        func1(str[:i]+str[i+1:],path + str[i], ans)


for i in range(T):
    str = sys.stdin.readline().rstrip()
    ans = []

    func1(str,"",ans)
    print(f"Case # {i+1}:")
    for a in ans:
        print(a)
