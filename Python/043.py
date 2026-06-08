# 문제: 약수 중 짝수의 합 구하기
# 입력: 정수 N
# 출력: N의 약수 중 짝수인 약수들의 합

N = int(input())
sum = 0
for i in range(1, N+1):
  if N % i == 0 and i % 2 == 0:
    sum += i
print(sum)
