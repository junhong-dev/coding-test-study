# 문제: 두 수의 나머지와 몫
# 입력: 공백으로 구분된 두 정수 A, B
# 출력: 첫째줄에 몫, 둘째줄에 나머지

a, b = map(int, input().split())
print(a // b)
print(a % b)
