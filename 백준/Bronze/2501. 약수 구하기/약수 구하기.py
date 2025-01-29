N, K = map(int, input().split())

def solution(N, K) :
    index = 0
    for i in range(1, N+1) :
        if N % i == 0 :
            index +=1
            if K == index :
                return i
    return 0

print(solution(N, K))