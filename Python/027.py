# 두 정수를 입력받아 두 수 사이의 짝수 개수를 출력하는 프로그램

# 입력:
# 두 정수 a, b

# 처리:
# a부터 b까지 반복하면서 짝수의 개수를 센다

# 출력:
# 두 수 사이의 짝수 개수

a, b = map(int, input().split())
sum = 0
for i in range(a, b + 1):
  if i % 2 == 0:
    sum += 1
print(sum)

