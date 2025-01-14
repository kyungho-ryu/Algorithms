from collections import deque
def solution(n, edge):
    graph = [[]  for _ in range(n+1)]

    for e1, e2 in edge :
        graph[e1].append(e2)
        graph[e2].append(e1)

    visited = [-1] * (n+1)
    queue = deque([(1, 0)])
    visited[1] = 0
    max_distance = 0
    while queue :
        node, distance = queue.popleft()

        max_distance = max(max_distance, distance)
        for neighbor in graph[node] :
            if visited[neighbor] == -1 :
                visited[neighbor] = distance +1
                queue.append((neighbor, distance+1))
    return visited.count(max_distance)


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])) # 3