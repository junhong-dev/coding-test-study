# 문제: 두 수의 평균과 차이
# 입력: 공백으로 구분된 두 정수 A, B
# 출력:
# 1. 두 수의 평균
# 2. 두 수의 차이의 절댓값

a, b = map(int, input().split())
print((a+b) / 2)
print(abs(b-a))
