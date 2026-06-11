# 문제: 가장 큰 진약수 구하기
# 입력: 정수 N (N >= 2)
# 출력: N의 약수 중 자기 자신을 제외한 가장 큰 수

N = int(input())
tmp = 0
for i in range(1, N+1):
  if N % i == 0 and i != N:
    tmp = i
print(tmp)
