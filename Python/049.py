# 문제: 진약수의 합 구하기
# 입력: 정수 N
# 출력: N의 진약수의 합

N = int(input())
sum = 0
for i in range(1, N+1):
  if N % i == 0 and i != N:
    sum += i
print(sum)
