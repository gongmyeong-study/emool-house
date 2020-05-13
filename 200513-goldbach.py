# 소수 구하는 함수  
def prime(a):
    i = 2
    while i < a/2:
        if a % i == 0:
            return False
        elif a == 2:
            return True
        elif a == 3:
            return True
        else:
            i = i + 1
    return True

# 정수 입력, 순서쌍 구하기
N = int(input())
a = int()
b = int()
prime_list = []

if 4 <= N <= 200000 and N % 2 == 0:
    for a in range(1, N):
        for b in range(1, N):
            if prime(a) is True and prime(b) is True:
                if a + b == N and a <= b:
                    prime_list.append((a, b))

# 순서쌍 출력
try:
    print(prime_list[0][0], prime_list[0][1]) 

except:
    pass

    





