a, b, c = map(int, input().split())
if b >= c:
    print(-1)
# 고정비용이 더 크면 손익 분기가 불가능
else:
    print((a // (c - b)) + 1)
# 이부분 이해가 잘 안가는데, 음.......  수직으로 이해하믄 된다.
# a + (b * x ) < c * x  -> a < (c-b) * x -> x > a//(c-b)되어야 하니까 +1


