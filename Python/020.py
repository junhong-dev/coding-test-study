# 문제: 세 수 중 가운데 값 찾기
# 입력: 공백으로 구분된 세 정수 A, B, C
# 출력: 세 수를 정렬했을 때 가운데 값

a, b, c = map(int, input().split())
print(a + b + c - max(a, b, c) - min(a, b, c))
