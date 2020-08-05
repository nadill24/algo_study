# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

test_case = int(input())

for t in range(test_case):
    a, b = map(int, input().split())
    sum = a + b
    print(f'Case #{t+1}: {a} + {b} = {sum}')