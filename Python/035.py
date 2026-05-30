# 입력: 세 자리 정수 1개
# 처리: 각 자리 숫자의 합 계산
# 출력: 각 자리 숫자의 합

a = int(input())
result = a // 100 + (a % 100) // 10 + a % 10
print(result)
