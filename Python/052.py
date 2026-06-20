# 문제: 소수 판별하기
# 입력: 정수 N
# 출력: N이 소수이면 Prime, 아니면 Not Prime

N = int(input())
is_prime = ""
for i in range(1, N+1):
  if N % i == 0 and i not in [1, N] or N == 1:
    is_prime = "Not Prime"
    break
  else:
    is_prime = "Prime"
print(is_prime)
