# 문제: 세 수를 오름차순으로 출력하기
# 입력: 공백으로 구분된 세 정수 A, B, C
# 출력: 세 수를 작은 수부터 큰 수 순서대로 출력
# 참고: 현재는 min/max로 풀이하며, 이후 배열(리스트)과 정렬을 배운 뒤 다시 구현 예정

a, b, c = map(int, input().split())
print(min(a, b, c), a + b + c - min(a, b, c) - max(a, b, c), max(a, b, c))
