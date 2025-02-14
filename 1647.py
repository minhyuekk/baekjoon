import sys
n, m = map(int, sys.stdin.readline().split())
parent = [_ for _ in range(n+1)]


def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y


def kruskal(edges):
    edges.sort(key=lambda x: x[2])
    total = 0
    selected = []

    for a, b, c in edges:
        if find(a) != find(b):
            union(a, b)
            total += c
            selected.append(c)

    total -= selected.pop()

    return total


edges = []
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((a, b, c))

print(kruskal(edges))
