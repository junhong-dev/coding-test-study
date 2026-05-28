# 입력:
# 두 정수 a, b
#
# 처리:
# 작은 수부터 큰 수까지 반복하면서
# 짝수만 골라 합산
#
# 출력:
# 두 수 사이 짝수의 합

a, b = map(int, input().split())
sum = 0
for i in range(min(a,b), max(a, b) + 1):
  if i % 2 == 0:
    sum += i
print(sum)
