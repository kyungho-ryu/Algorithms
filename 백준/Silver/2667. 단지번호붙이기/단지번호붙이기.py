from collections import deque
import heapq
N = int(input())
maps = []
for _ in range(N) :
    maps.append(input())

def solution(N, maps):
    visited = [[False] * N for _ in range(N)]
    actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(x, y):
        queue = deque()
        count = 1
        queue.append([x, y])
        visited[y][x] = True

        while queue :
            x, y = queue.popleft()
            for dx, dy in actions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N:
                    if maps[ny][nx] == '1' and not visited[ny][nx]:
                        queue.append([nx, ny])
                        visited[ny][nx] = True
                        count +=1
        return count

    result = []
    for y in range(N):
        for x in range(N):
            if maps[y][x] == '1' and not visited[y][x]:
                heapq.heappush(result, bfs(x, y))
    print(len(result))
    for _ in range(len(result)) :
        print(heapq.heappop(result))


solution(N, maps)