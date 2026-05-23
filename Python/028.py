# 두 정수를 입력받음
# 홀수의 개수를 저장할 변수를 생성
# a부터 b까지 반복하면서 홀수인지 확인
# 홀수라면 개수를 증가
# 최종 홀수 개수 출력

a, b = map(int, input().split())
sum = 0
for i in range(a, b + 1):
  if i % 2 != 0:
    sum += 1
print(sum)
