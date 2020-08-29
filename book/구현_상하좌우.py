

n = int(input()) # 좌표 칸 규격

la = list(input().split()) # 상하좌우 명령어

startpoint = [1, 1] # 시작점

for i in la:
    if i == 'R':
        if startpoint[0] < n:  # n보다 작을경우 우로 이동
            startpoint[0] +=1
    if i == 'l':
        if startpoint[0] > 1: # 1보다 클경우 좌로 이동
            startpoint[0] -= 1
    if i == 'D':
        if startpoint[1] < n: # n보다 작을경우 아래로 이동
            startpoint[1] += 1
    if i == 'U':
        if startpoint[1] > 1: # 1보다 클경우 위로 이동
            startpoint[1] -= 1


print(startpoint[1], startpoint[0])

