# 소수 구하는 함수  
def decimal(a):
    if a % 2 != 0 and a % 3 != 0 and a**0.5 != int:
        return True
    elif a == 2:
        return True

# 정수 입력, 순서쌍 구하기
N = int(input())
a = int()
b = int()
decimal_list = []

if 4 <= N <= 200000 and N % 2 == 0:
    for a in range(1, N):
        for b in range(1, N):
            if decimal(a) is True and decimal(b) is True:
                if a + b == N and a <= b:
                    decimal_list.append((a, b))

# 순서쌍 출력
try:
print(decimal_list[0][0], decimal_list[0][1]) 

except:
    pass

    





