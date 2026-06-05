# 문제: 약수의 합 구하기
# 입력: 정수 N
# 출력: N의 모든 약수의 합

N = int(input())
sum = 0
for i in range(1, N+1):
  if N % i == 0:
    sum += i
print(sum)
