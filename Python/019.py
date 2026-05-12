# 문제: 큰 수에서 작은 수 빼기
# 입력: 공백으로 구분된 두 정수 A, B
# 출력: 큰 수 - 작은 수 결과

a, b = map(int, input().split())
print(max(a,b) - min(a, b))
