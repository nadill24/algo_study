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

#교제 풀이
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