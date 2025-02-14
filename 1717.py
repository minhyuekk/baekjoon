import sys
n, m = map(int, sys.stdin.readline().split())
parent = [_ for _ in range(n+1)]


# x가 속한 집합의 대표 찾기
def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


# x와 y가 속한 두 집합을 합침
def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        if root_x > root_y:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y


for _ in range(m):
    op, a, b = map(int, sys.stdin.readline().split())

    if op == 0:  # 합집합 연산
        union(a, b)
    elif op == 1:  # 같은 집합에 속하는지 확인하는 연산
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")


