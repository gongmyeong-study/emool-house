import sys

# 정수 입력
N = int(input())
if 3 <= N <= 3000 and N % 3 == 0:
    pass
else:
    print("N은 3이상 3000이하인 3의 배수여야 합니다.")
    sys.exit()


# 정수 N 길이의 염기서열 입력
sequence = input()

if len(sequence) == N:
    pass
else:
    print("N의 길이만큼 염기서열을 입력하세요.")
    sys.exit()

# 염기서열 성분 검사

for a in sequence:
    if a == 'A' or a == 'C' or a == 'G' or a == 'T':
        pass
    else:
        print("염기서열은 A, C, G, T로만 이루어져야 합니다.")
        sys.exit()

# 염기서열 트리플렛 코드 읽기  

i = 0
triplet_sequence = []
while i + 2 < N:
    triplet_sequence.append(tuple(sequence[i:i+3]))
    i += 3

# 트리플렛 코드 대칭 확인하기 
i = 0
while i <N/3/2:
    if triplet_sequence[i] == triplet_sequence[int(N/3) - i - 1]:
        pass 
    else:
        print('FALSE')
        sys.exit()
    i += 1

print('TRUE')