# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#
#
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.
#
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
#
# 입력의 마지막에는 0 두 개가 들어온다.

a=10
b=10

while a != 0 and b !=0:

    a, b = map(int, input().split())
    if a== 0 and b==0:
        break
    else:
        print(a+b)

# 다른사람 코드

import sys

while True: # 0이 아닌건 트루니까.. .ㅇㅅㅇ 이거 하면 a, b값 안줘도 댐 근데 true가 뭔 말인지 정확히는 모르겠다...
	(a, b) = map(int, sys.stdin.readline().split())
	if (a == 0 and b == 0):
		break
	print(a+b)

