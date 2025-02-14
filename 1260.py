from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    que = deque([start])
    visited[start] = True
    while que:
        v = que.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True


visited_dfs = [0] * (n+1)
visited_bfs = [0] * (n+1)
dfs(graph, v, visited_dfs)
print("")
bfs(graph, v, visited_bfs)