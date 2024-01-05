N = int(input())

count =0
idx= 0
while(1):
    if "666" in str(idx):
        count += 1
    if count == N:
        print(idx)
        break
    idx += 1