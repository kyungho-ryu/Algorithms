from collections import deque

def solution(maps):
    actions = [[-1,0], [1,0], [0, -1], [0, 1]]
    queue = deque([(0,0,1)])
    n, m = len(maps), len(maps[0])
    vistied = [[False] * m for _ in range(n)]
    vistied[0][0] = True

    while queue :
        x,y,count = queue.popleft()

        if x == n-1 and y == m-1 :
            return count

        for dx, dy in actions :
            nx, ny = x+dx, y + dy

            if 0 <=nx < n and 0<=ny < m and not vistied[nx][ny] and maps[nx][ny] == 1 :
                vistied[nx][ny] = True
                queue.append((nx, ny, count+1))

    return -1

# 제한사항
# maps는 n x m 크기의 게임 맵의 상태가 들어있는 2차원 배열로, n과 m은 각각 1 이상 100 이하의 자연수입니다.
# n과 m은 서로 같을 수도, 다를 수도 있지만, n과 m이 모두 1인 경우는 입력으로 주어지지 않습니다.
# maps는 0과 1로만 이루어져 있으며, 0은 벽이 있는 자리, 1은 벽이 없는 자리를 나타냅니다.
# 처음에 캐릭터는 게임 맵의 좌측 상단인 (1, 1) 위치에 있으며, 상대방 진영은 게임 맵의 우측 하단인 (n, m) 위치에 있습니다.

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])) # 11
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])) # -1
