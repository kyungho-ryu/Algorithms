def solution(n, computers):
    def dfs(i, visited) :
        visited[i] = True
        for j in range(n) :
            if not visited[j] and computers[i][j] ==1 :
                dfs(j, visited)

    answer = 0
    visited = [False] * n
    for i in range(n) :
        if not visited[i] :
            dfs(i, visited)
            answer +=1

    return answer

# 제한사항
# 컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
# 각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
# i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
# computer[i][i]는 항상 1입니다.

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]	)) # 1