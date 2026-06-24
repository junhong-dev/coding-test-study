# 문제: 범위 안의 가장 작은 소수 찾기
# 입력: 두 정수 A, B (A ≤ B)
# 출력: A 이상 B 이하의 소수 중 가장 작은 수
# 단, 소수가 없으면 -1 출력

A, B = map(int, input().split())
is_prime = "Y"
c = -1
for i in range(A, B+1):
  for j in range(1, i+1):
    if (i % j == 0 and j not in [1, i] or i == 1): # () 조건 = 합성수이거나 1
      is_prime = "N"
      break
  if is_prime == "Y":
    c = i
    break
  is_prime = "Y"
print(c)
    
