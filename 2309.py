height = []
sum = 0

for _ in range(9):
    n = int(input())
    height.append(n)
    sum += n

for i in range(8):
    for j in range(i+1, 9):
        if sum - (height[i] + height[j]) == 100:
            del height[j], height[i]
            break
    if len(height) == 7:
        break

height.sort()
for res in height:
    print(res)