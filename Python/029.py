# 입력:
# - 서로 다른 두 정수 a, b를 입력받음
#
# 처리:
# - a부터 b까지 반복하면서
# - 3으로 나누어 떨어지는 수의 개수를 셈
#
# 출력:
# - 3의 배수 개수 출력

a, b = map(int, input().split())
sum = 0
for i in range(a, b+1):
  if i % 3 == 0:
    sum += 1
print(sum)
