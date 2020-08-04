# int(sys.stdin.readline()), sys.stdin.readline().split()

import sys


test_case = int(input())

for t in range(test_case):
    a, b = map(int, sys.stdin.readline().split())
    sum = a + b
    print(sum)


inp = int(input())
for i in range(inp):
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)
