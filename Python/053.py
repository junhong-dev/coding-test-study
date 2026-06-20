# 문제: 범위 안의 소수 개수 구하기
# 입력: 정수 A, B
# 출력: A 이상 B 이하의 소수의 개수

A, B = map(int, input().split())
C = B - A + 1
for i in range(A, B+1):
  for j in range(1, i+1):
    if i % j == 0 and j != i and j != 1 or i == 1:
      C -= 1
      break
print(C)
