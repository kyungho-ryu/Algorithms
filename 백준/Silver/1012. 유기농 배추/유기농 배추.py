from collections import deque

T = int(input())
answer = []
for _ in range(T) :
    M, N, K = map(int, input().split())
    target = []
    for _ in range(K) :
        target.append(list(map(int, (input().split()))))


    def solution(M, N, K, target):
        visited = [False] * K
        actions = [[-1,0], [1,0],[0,-1],[0,1]]
        queue = deque()
        answer = 0

        for i in range(K) :
            if not visited[i] :
                queue.append(target[i])
                visited[i] = True
                while queue :
                    x0, y0 = queue.popleft()
                    for dx, dy in actions :
                        new_target = [x0 + dx, y0+dy]
                        if new_target in target :
                            _index = target.index(new_target)
                            if not visited[_index] :
                                queue.append(new_target)
                            visited[_index] = True

                answer +=1
        return answer

    answer.append(solution(M, N, K, target))

for i in answer :
    print(i)