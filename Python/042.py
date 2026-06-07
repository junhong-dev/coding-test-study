# 문제: 약수 중 홀수의 개수 구하기
# 입력: 정수 N
# 출력: N의 약수 중 홀수의 개수

N = int(input())
count = 0 
for i in range(1, N+1): 
  if N % i == 0 and i % 2 == 1: 
    count += 1 
print(count)
