def solution(n, results):
    answer = 0
    graph = [[0] * (n+1) for _ in range(n+1)]

    for winer, loser in results :
        graph[winer][loser] = 1
        graph[loser][winer] = -1

    for i in range(1, n+1) :
        for j in range(1, n+1) :
            for k in range(1, n+1) :
                if graph[j][i] == 1 and graph[i][k] == 1 :
                    graph[j][k] = 1
                if graph[j][i] == -1 and graph[i][k] == -1 :
                    graph[j][k] = -1

    for i in range(1, n+1) :
        if graph[i].count(0) == 2: answer +=1
    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))  # 2

# [1] = [0, 1, 0, 0, 1]
# [2] = [-1, 0, -1, -1, 1]
# [3] = [0, 1, 0, -1, 1]
# [4] = [0, 1, 0, 0, 1]
# [5] = [0, -1, 0, 0, 0]
