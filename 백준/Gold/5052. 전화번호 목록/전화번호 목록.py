import sys

t = int(sys.stdin.readline())

for _ in range(t):
    answer = "YES"
    d = {}
    n = int(sys.stdin.readline())
    for _ in range(n):

        str = sys.stdin.readline().rstrip()
        if not str or answer == "NO": continue

        pre_dict = d
        if str[0] not in pre_dict:
            for s in str:
                pre_dict[s] = {}
                pre_dict = pre_dict[s]
        else:
            for i,s in enumerate(str):
                #있으면 들어감
                if s in pre_dict:
                    pre_dict = pre_dict[s]
                #길이 끊기면
                else:
                    #다른 애들도 없으면(분기가 안됨)
                    if len(pre_dict) == 0:
                        answer = "NO"
                        break
                    #분기가 되면
                    for ss in str[i:]:
                        pre_dict[ss] = {}
                        pre_dict = pre_dict[ss]
                    break
            else:
                answer = "NO"
    print(answer)
