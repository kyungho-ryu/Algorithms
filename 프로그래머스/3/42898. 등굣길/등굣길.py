def solution(m, n, puddles):
    # DP 테이블 초기화
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1  #

    # 물에 잠긴 지역을 집합으로 변환
    puddles = {(x, y) for x, y in puddles}

    # DP 테이블 채우기
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if (x, y) in puddles or (x == 1 and y == 1):
                # 물에 잠긴 곳 또는 시작점은 처리하지 않음
                continue
            dp[y][x] = (dp[y - 1][x] + dp[y][x - 1]) % 1000000007  # 위 + 왼쪽
    return dp[n][m]  # 도착점의 경로 개수 반환


# 테스트
print(solution(4, 3, [[2, 2]]))  # 출력: 4
