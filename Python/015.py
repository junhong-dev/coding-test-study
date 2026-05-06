# 문제: 세 수 중 최솟값
# 입력: 공백으로 구분된 세 정수 A, B, C
# 출력: A, B, C 중 가장 작은 값을 출력

a, b, c = map(int, input().split())
print(min(a,b,c))
