from collections import deque
# (1, 1)에서 (N, M)의 위치까지 최단거리
# 시작하는 칸과 끝나는 칸도 포함
# 벽을 한 개 까지 부수고 이동 가능
# 상하좌우로

N, M = map(int, input().split()) # 1~1000
maps = [input() for _ in range(N)]

def my_print(arr) :
    for row in arr :
        print(row)
    print("--------------------------------------------------------------")

def solution(maps) :
    Q = deque()
    visited = [[[False]*2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = True
    Q.append([[0,0], False, 1]) # 위치, 방문, 벽부셧는지, 이동횟수

    while Q :
        pos, flag, dist = Q.popleft()
        cx, cy = pos
        if cx == M-1 and cy == N-1 :
            return dist

        for dx, dy in [(-1,0), (1,0), (0,-1), (0, 1)] :
            nx, ny = cx+dx, cy+dy
            if 0<=nx<M and 0<=ny<N:
                if maps[ny][nx] == '0' and not visited[ny][nx][flag]:
                    visited[ny][nx][flag] = True
                    Q.append([[nx, ny], flag, dist+1])
                elif maps[ny][nx] == '1' and not flag and not visited[ny][nx][1] :
                    visited[ny][nx][1] = True
                    Q.append([[nx, ny], True, dist+1])

    return -1
print(solution(maps)) # 15