from collections import deque


def solution(maps):
    def bfs(maps, pos):
        visitied = [[False] * len(maps[0]) for _ in range(len(maps))]
        visitied[pos[0]][pos[1]] = True

        queue = deque([[pos[0], pos[1], 0]])
        while queue:
            x, y, _sum = queue.popleft()
            _sum += 1

            if y == len(maps)-1 and x == len(maps[0])-1:
                return _sum

            if x - 1 >= 0 and not visitied[y][x - 1] and maps[y][x-1] == 1:
                queue.append([x - 1, y, _sum])
                visitied[y][x - 1] = True
            if x + 1 < len(maps[0]) and not visitied[y][x + 1] and maps[y][x+1] == 1:
                queue.append([x + 1, y, _sum])
                visitied[y][x + 1] = True
            if y - 1 >= 0 and not visitied[y - 1][x] and maps[y-1][x] == 1:
                queue.append([x, y - 1, _sum])
                visitied[y - 1][x] = True
            if y + 1 < len(maps) and not visitied[y + 1][x] and maps[y+1][x] == 1:
                queue.append([x, y + 1, _sum])
                visitied[y + 1][x] = True

    result = bfs(maps, (0, 0))
    return result if result else -1


maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps))