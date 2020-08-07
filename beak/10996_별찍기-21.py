# 문제
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
#
# 출력
# 첫째 줄부터 차례대로 별을 출력한다.

t = int(input())

if t ==1 :
    print('*')
else:
    if t%2 !=0:
        for i in range(t):
            print("*" +' *'*int(((t-1)/2)))
            print(" *"*(t-int(((t+1)/2)) ))
    if t%2 ==0:
        for i in range(t):
            print("*" + ' *'*int((t-1)/2))
            print(' *'*int(t/2))



