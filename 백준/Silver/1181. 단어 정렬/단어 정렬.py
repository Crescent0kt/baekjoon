import sys

N = int(sys.stdin.readline())
word_set = set()
for _ in range(N):
    word_set.add(sys.stdin.readline().rstrip())

for word in sorted(list(word_set), key=lambda x:(len(x),x)):
    print(word)
