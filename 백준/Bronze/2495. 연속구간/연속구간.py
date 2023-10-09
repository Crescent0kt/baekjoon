arr = []
for _ in range(3):
    s = input()
    count = 1
    maximum = 1
    check = s[0]
    for i in range(1,len(s)):
        if s[i] == check:
            count +=1
        else:
            check = s[i]
            if maximum < count: maximum = count
            count = 1
    if maximum < count: maximum = count
    arr.append(maximum)

for i in arr:
    print(i)