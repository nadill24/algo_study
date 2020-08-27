# testcase1
# 25 5
#


n, m = map(int, input().split())

cnt = 0

while n != 1:
    if n % m == 0:
        n = n // m
        cnt +=1
    else:
        n -= 1
        cnt +=1

print(cnt)

#교제 풀이

n, m = map(int, input().split())

cnt = 0

# m이 m 이상이라면 m으로 계속 나누기
while n >= m:
    # 나누어지지 않을 경우
    while n % k != 0:
        n -= 1
        cnt +=1
    # m으로 나누기
    n //= m
    cnt += 1

# 마지막으로 다 나누고 남은 수에 대해서 1씩 빼기
while n > 1:
    n -= 1
    cnt +=1

print(cnt)

# 숫자가 커질 경우 시간이 오래 걸린다 이걸 한번에 하자

n, m = map(int, input().split())

cnt = 0

while True:
    # 나누어 질때 까지 1 씩 뺴기
    target = (n // m) * m
    cnt += (n - target)
    n = target
    # n이 m보다 작을 때 반복문 탈출

    if n < m:
        break
    cnt += 1
    n //= m

# 마지막으로 남은 수에 대하여 1씩 뺴기
cnt += (n-1) # 28 5 일 경우 3이 남는데 1과의 차만큼(2) 뺀다
print(cnt)