import heapq
import sys

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    num = int(sys.stdin.readline())

    if num == 0 and not heap:
        print(0)
    elif num == 0:
        print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, num)

