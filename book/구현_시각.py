'''
정수 n이 입력되면 00시 00분 00초부터 n시 00시 00분까지 모든 시각 중에서 3이 들어간 모든 경우의 수를 구하여라

조건 3이 들어가면 무조건 카운트 시 분 초에 3이 중복 될수 있음 중복되는 경우 다 빼야 함

시간 부터 조건을 차례대로 구현하자
'''

n = int(input())

# n이 3일 때 총 경우의 수는 60 * 60
# n이 3이 아닐 때 분에 3이 있을 경우 3 13 23 30번대 43 53 > 15 * 60
# 초에 3이 있을 경우 3 13 23 30번대 43 53 15개
# 15 * 60 + 45 * 15

cnt = 0
for i in range(0, n+1):
    if i == 0:
        cnt += 15 * 60 + 45 * 15
    else:
        if i % 3 == 0:
            cnt += 60 * 60
        else:
            cnt += 15 * 60 + 45 * 15

print(cnt)


# 교제 풀이

h = int(input())
count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count +=1

print(count)