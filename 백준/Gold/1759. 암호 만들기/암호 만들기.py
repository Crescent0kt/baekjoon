import sys

L,C = map(int,sys.stdin.readline().split())
alphabet = sys.stdin.readline().split()
alphabet.sort()
answer = []

aeiou = -1
for i,alpha in enumerate(alphabet):
    if alpha in ["a","e","i","o","u"]:
        aeiou = max(aeiou,i)

def dfs(index,path,count):

    if len(path)>=L:
        #자음 수가 2보다 크면.
        if len(path) - count >=2 and count >=1:
            print("".join(path))
        return

    for i in range(index, C):
        #현재까지 길이 + 알파벳 남은 길이 < 내가 필요한 문자열 길이 : break
        if len(path) + len(alphabet) - i <L:
            break
        elif i > aeiou and count == 0:
            break
        else:
            if alphabet[i] in ["a","e","i","o","u"]:
                dfs(i+1, path + [alphabet[i]],count+1)
            else:
                dfs(i + 1, path + [alphabet[i]], count)

dfs(0,[],0)
