from collections import deque

N, M, V = map(int, input().split(" "))
graph = [[False] * (N+1) for _ in range(N+1)]
for _ in range(M) :
    n1, n2 = map(int, input().split(" "))
    graph[n1][n2] = True
    graph[n2][n1] = True

def dfs(graph, v, visited) :
    print(v, end=" ")
    for i, neighbor in enumerate(graph[v]) :
        if neighbor and not visited[i] :
            visited[i] = True
            dfs(graph, i, visited)

def bfs(graph, start) :
    visited = [False] * (N + 1)
    queue = deque([start])
    visited[start] = True

    while queue :
        v = queue.popleft()
        print(v, end=" ")

        for i, neighbor in enumerate(graph[v]) :
            if neighbor and not visited[i] :
                queue.append(i)
                visited[i] = True


def solution(N, M, V, graph) :
    visited = [False] * (N + 1)
    visited[V] = True
    dfs(graph, V, visited)
    print()
    bfs(graph, V)

solution(N, M, V, graph)
