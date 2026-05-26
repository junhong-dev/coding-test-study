# 입력:
# 두 정수 a, b
#
# 출력:
# a부터 b까지의 수 중
# 5의 배수의 합
#
# 설명:
# 반복문으로 범위를 순회하면서
# 5의 배수만 더함

a, b = map(int, input().split())
sum = 0
for i in range(a, b + 1):
  if i % 5 == 0:
    sum += i
print(sum)
