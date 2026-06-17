# 문제: 완전수 판별하기
# 입력: 정수 N
# 출력: N이 완전수이면 Perfect, 아니면 Not Perfect

N = int(input())
r = 0
for i in range(1, N+1):
  if N % i == 0 and i != N:
    r += i
if r == N:
  print("Perfect")
else:
  print("Not Perfect")
