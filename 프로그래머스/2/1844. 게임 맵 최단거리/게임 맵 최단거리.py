from collections import deque

def solution(maps):
    visitied = [[False] * len(maps[0]) for _ in range(len(maps))]
    queue = deque([(0,0,1)])
    visitied[0][0] = True

    while queue:
        x, y, sum = queue.popleft()
        if x == (len(maps[0]) - 1) and y == (len(maps) - 1):
            return sum

        for _x, _y in [(-1,0), (1,0), (0,-1), (0,1)] :
            new_x = x+_x
            new_y = y+_y
            if new_x >= 0 and new_x <len(maps[0]) and new_y >=0 and new_y <len(maps) and maps[new_y][new_x] == 1 :
                if not visitied[new_y][new_x] :
                    v = new_x, new_y, sum+1
                    queue.append(v)
                visitied[new_y][new_x] = True


    return -1

print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))