# 문제: 절댓값이 더 큰 수
# 입력: 공백으로 구분된 두 정수 A, B
# 출력: |A|와 |B| 중 더 큰 값을 출력

a, b = map(int, input().split())
print( max( abs(a), abs(b) ) )
