import math
# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
# 1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 2. X가 2로 나누어 떨어지면, 2로 나눈다.
# 3. 1을 뺀다.

N = int(input())  # 1~10^6

# 1을 만들기 위한 최솟값
# 1을 만들기 위해 거쳐가는 수
def solution(N):
    dp = [0 for _ in range(N + 1)]
    path = [[1] for _ in range(N + 1)]
    dp[1] = 0

    # N = 4
    for i in range(2, N + 1):  # 2, 3, 4
        candidate = [i-1]
        if i % 2 == 0 :
            candidate.append(int(i/2))
        if i % 3 == 0 :
            candidate.append(int(i/3))

        min_index = 0
        min_v = math.inf
        for candi in candidate :
            if dp[candi] + 1 < min_v :
                min_v = dp[candi] +1
                min_index = candi

        dp[i] = min_v
        path[i] = path[min_index] + [i]

    print(dp[N])
    for n in range(len(path[N])-1,-1,-1):
        print(path[N][n], end=" ")


solution(N)  # 10 -> 3, 10 9 3 1