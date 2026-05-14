# 문제: 세 수의 차이 중 최댓값
# 입력: 공백으로 구분된 세 정수 A, B, C
# 출력: |A-B|, |A-C|, |B-C| 중 가장 큰 값

a, b, c = map(int, input().split())
print(max(abs(a-c), abs(a-b), abs(b-c))
