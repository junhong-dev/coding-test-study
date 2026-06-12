주석
# 문제: 약수 중 가장 작은 짝수 약수 구하기
# 입력: 정수 N
# 출력: N의 약수 중 가장 작은 짝수 약수
#       짝수 약수가 없으면 0

N = int(input())
tmp = 0
for i in range(1, N+1):
  if N % i == 0 and i % 2 == 0:
    tmp = i
    break
print(tmp)
