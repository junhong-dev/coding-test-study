# 문제: 두 수 사이의 정수 개수
# 입력: 공백으로 구분된 서로 다른 두 정수 A, B
# 출력: A와 B 사이에 있는 정수의 개수 (A, B 제외)

a, b = map(int, input().split())
print(max(a, b) - min(a,b) - 1)
