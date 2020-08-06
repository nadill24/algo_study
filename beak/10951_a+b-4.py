# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.
#
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

a = 10
b = 10

while a != False and b != False:
    a, b = map(int, input().split())
    print(a+b)

# 이렇게 하면 안된다 무한루프에 빠지기 때문에

# so1 1

while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break

# sol2

import sys

for i in sys.stdin:
    a, b = map(int, i.split())
    print(a+b)