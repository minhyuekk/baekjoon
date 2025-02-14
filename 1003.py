import sys
t = int(sys.stdin.readline())


def fib(n):
    a, b = 1, 0
    for i in range(n):
        a, b = b, a+b
    print(a, b)


for _ in range(t):
    n = int(input())
    fib(n)