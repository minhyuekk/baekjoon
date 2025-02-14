import sys

n = int(sys.stdin.readline())
graph = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

# arr: 각 노드의 부모 노드를 적은 리스트, d: 삭제할 노드
def dfs(arr, d):
    # 삭제되는 노드의 값을 -2로 선언
    arr[d] = -2
    # 부모 노드가 삭제되면 그 노드 번호를 값으로 가진 자식 노드들도 같이 삭제되어야 함
    for i in range(n):
        if arr[i] == d:
            # 그 아래의 자식노드들도 탐색하고 삭제하기 위해 재귀호출
            dfs(arr, i)


dfs(graph, m)
res = 0
for i in range(n):
    # 삭제되지 않은 노드들 중 리스트의 인덱스를 값으로 가진 인덱스가 없다면 해당 노드는 자식이 없는 노드
    if graph[i] != -2 and i not in graph:
        res += 1

print(res)
