from collections import deque

M, N = map(int, input().split())
maps = []
for _ in range(N) :
    maps.append(list(map(int, input().split())))

def solution(M, N, maps):
    visited = [[False] * M for _ in range(N)]
    actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()

    target = M * N
    for n in range(N) :
        for m in range(M) :
            if maps[n][m] == 1 :
                queue.append((m,n))
                visited[n][m] = True
                target -=1
            elif maps[n][m] == -1 :
                target -=1

    def bfs(queue, target):
        new_queue = deque()

        while queue :
            x, y = queue.popleft()
            for dx, dy in actions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < M and 0 <= ny < N:
                    if maps[ny][nx] != -1 and maps[ny][nx] == 0 and not visited[ny][nx]:
                        new_queue.append([nx, ny])
                        visited[ny][nx] = True
                        maps[ny][nx] = 1
                        target -=1
        return new_queue, target


    count = -1
    while queue :
        new_queue, new_target = bfs(queue, target)
        queue = new_queue
        target = new_target
        count +=1

    print (count if target ==0 else -1)


solution(M, N, maps)