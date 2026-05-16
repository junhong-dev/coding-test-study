# 문제: 세 수 정렬하기
# 입력: 공백으로 구분된 세 정수 A, B, C
# 출력:
# 첫째 줄에 가장 작은 수
# 둘째 줄에 가운데 수
# 셋째 줄에 가장 큰 수 출력

a, b, c = map(int, input().split())
print(min(a, b, c))
print(a + b + c - max(a, b, c) - min(a, b, c))
print(max(a, b, c))
