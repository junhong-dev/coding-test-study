# 문제: 약수가 가장 많은 수 찾기
# 입력: 정수 A, B
# 출력: A 이상 B 이하의 수 중 약수의 개수가 가장 많은 수

A, B = map(int, input().split())
tmp = 0
c1 = 0
c2 = 0
for i in range(A, B+1):
  for j in range(1, i+1):
    if i % j == 0:
      c1 += 1
  if c1 > c2 :
    c2 = c1
    tmp = i
  c1 = 0
print(tmp)
