def find_hansu(a):
    cnt = 0
    for i in range(1, a+1):
        num = list(map(int, str(i)))
        if i < 100:
            cnt += 1
        elif i <= 1000:
            if num[0] - num[1] == num[1] - num[2]:
                cnt += 1
    return cnt

n = int(input())
print(find_hansu(n))