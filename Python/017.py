# 문제: 두 수 중 큰 수와 작은 수 출력
# 입력: 공백으로 구분된 두 정수 A, B
# 출력: 첫째 줄에 더 큰 수, 둘째 줄에 더 작은 수

a, b = map(int, input().split())
print(max(a, b), min(a, b), sep="\n")
