# 문제: 두 수 사이의 짝수 개수 구하기
# 입력: 공백으로 구분된 두 정수 A, B
# 출력: A와 B 사이(양 끝 제외)에 있는 짝수의 개수

a, b = map(int, input().split())
c = (max(a,b) - min(a,b)) // 2
if(a % 2 == 0 and b % 2 == 0):
  c -= 1
print(c)
