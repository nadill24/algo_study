# testcase1
# 5 8 3
# 2 4 5 4 6
# textcase2
# 5 7 3
# 3 4 3 4 3


n, m, l = map(int, input().split())

la = list(map(int, input().split()))
sum = 0

sa = sorted(la, reverse=True) # 역순으로 정렬

cnt = 0

while cnt != m:
    for i in range(l): #최대 개수 까지 가장 큰수 더하기
        sum += sa[0]
        cnt +=1
    if cnt !=m: # 충족 안됐을 경우, 두번째로 큰수 한번 더하기
        sum += sa[1]
        cnt +=1

print(sum)

#교제 풀이 단순 코드
n, m, l = map(int, input().split())

la = list(map(int, input().split()))
la.sort() # 정렬
first = la[n-1] # 가장 큰수
second = la[n-2] # 두번째 큰수
result = 0
while True:
    for i in range(l):
        if m == 0: #m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1 #더할때마다 1씩 빼기
    if m ==0:
        break
    result += second
    m -= 1

print(result)

# 좀더 생각해보자 수열로 생각했을 경우
n, m, l = map(int, input().split())

la = list(map(int, input().split()))
la.sort() # 정렬
first = la[n-1] # 가장 큰수
second = la[n-2] # 두번째 큰수

#가장 큰 수가 더해지는 횟수 계산
count = int(m / (l + 1))*l
# 최대연속갯수 + 두번째로 작은수를 한 싸이클로 보고 몇번 반복되는 값을 구한후 다시 l을 곱하면 가장 큰수가 나오는 횟수가 된다.
count += m % (k+1)
#나머지 만큼 더한값

result1 = 0
result1 += count * (first)
result1 += (m-count) * second
print(result1)