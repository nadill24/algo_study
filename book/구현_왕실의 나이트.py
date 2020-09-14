'''
testdata = a1 > 2
'''



# 우선 둘다 숫자라 생각하자. 0, 0 처럼

a = [0, 0]

move_point = [[2,1], [2,-1], [-2, 1], [-2, -1],
              [1, -2], [1, 2], [-1, 2], [-1, -2]]

cnt = 0
new= [0, 0]
for i in range(8):
    new[0] = a[0] + move_point[i][0]
    new[1] = a[1] + move_point[i][1]
    if new[0] >= 0 and new[0] < 8 and new[1] >= 0 and new[1] < 8:
        cnt +=1

print(cnt)

# 문자일 때

b = list(input())
col = int(ord(b[0])) - int(ord('a')) + 1
cnt = 0
new = [0, 0]
move_point = [[2,1], [2,-1], [-2, 1], [-2, -1],
              [1, -2], [1, 2], [-1, 2], [-1, -2]]

for i in range(8):
    new[1] = int(b[1]) + move_point[i][1]
    new[0] = col + move_point[i][0]
    if new[0] >= 1 and new[0] < 9 and new[1] >= 1 and new[1] < 9:
        cnt += 1


print(cnt)