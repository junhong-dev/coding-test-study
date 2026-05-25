# 입력:
# a, b, k (시작값, 끝값, 기준 배수)
#
# 처리:
# a부터 b까지 반복하면서
# k의 배수이면 개수를 증가시킴
#
# 출력:
# k의 배수 개수

a, b, k = map(int, input().split())
sum = 0
for i in range(a, b + 1):
  if i % k == 0:
    sum += 1
print(sum)
