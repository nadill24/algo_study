    # testcase1
    # 3 3
    # 3 1 2
    # 4 1 4
    # 2 2 2
    # testcase2
    # 2 4
    # 7 3 1 8
    # 3 3 3 4

n, m = map(int, input().split())
la = []
for i in range(n):
    la.append(list(map(int, input().split())))
sa = [] # 각 행의 최소값을 넣은 리스트 만들기
for i in range(n):
    sa.append(min(la[i]))
print(max(sa)) # 그중 최대값 출력

#min max 활용법
n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value) # 이표현법은 처음이네 신기

print(result)

#2중 반복문 구조 이용
n, m = map(int, input().split())
for i in range(n):
    data = list(map(int, input().split()))
    mv = 10001 # 문제에서 주어진 값보다 가장 큰 값
    for a in data:
        mv = min(mv, a)
    result = max(result, mv)

print(result)