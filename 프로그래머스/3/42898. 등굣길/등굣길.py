from collections import deque

# (1,1) (m,n)
m = 4
n = 3
# puddles: 물에 잠긴 지역의 좌표들 (2차원 배열)
puddles = [[2,2]]

def my_print(arr) :
    for row in arr :
        print(row)

    print("---------------------------------------")

def solution(m,n,puddles):
    visitied = [[0 for _ in range(m)] for _ in range(n)]
    queue = deque()
    queue.append([0,0])
    visitied[0][0] = 1
    set_puddles = {(x, y) for x, y in puddles}

    while queue :
        cx, cy = queue.popleft()

        if cx == m-1 and cy == n-1 :
            continue

        for dx, dy in [(1,0), (0,1)] :
            tx, ty = cx+dx, cy+dy
            if 0<=tx<m and 0<=ty<n and (tx+1, ty+1) not in set_puddles:
                if visitied[ty][tx] == 0 :
                    queue.append([tx, ty])

                visitied[ty][tx] += visitied[cy][cx]
        # my_print(visitied)
    # 오른쪽과 아래쪽으로만 움직여 학교까지 갈 수 있는 최단경로의 갯수를 1,000,000,007로 나눈 나머지 return
    return visitied[n-1][m-1] % 1000000007


# def solution(m, n, puddles):
#     # DP 테이블 초기화
#     dp = [[0] * (m + 1) for _ in range(n + 1)]
#     dp[1][1] = 1  #
#
#     # 물에 잠긴 지역을 집합으로 변환
#     puddles = {(x, y) for x, y in puddles}
#
#     # DP 테이블 채우기
#     for y in range(1, n + 1):
#         for x in range(1, m + 1):
#             if (x, y) in puddles or (x == 1 and y == 1):
#                 # 물에 잠긴 곳 또는 시작점은 처리하지 않음
#                 continue
#             dp[y][x] = (dp[y - 1][x] + dp[y][x - 1]) % 1000000007  # 위 + 왼쪽
#     return dp[n][m]  # 도착점의 경로 개수 반환


# 테스트
print(solution(4, 3, [[2, 2]]))  # 출력: 4


print(solution(m,n,puddles)) # 4
