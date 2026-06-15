# 문제: 약수 중 가장 큰 홀수 약수 구하기
# 입력: 정수 N
# 출력: N의 약수 중 가장 큰 홀수 약수

N = int(input())
tmp = 0
for i in range(1, N+1):
  if N % i == 0 and i % 2 == 1:
    tmp = i
print(tmp)
