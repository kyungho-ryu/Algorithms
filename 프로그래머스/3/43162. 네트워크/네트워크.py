from collections import deque

def get_node(computer, visited) :
    temp = []
    for i, v in enumerate(computer) :
        if v and not visited[i] :
            temp.append(i)

    return temp

def solution(n, computers) :
    answer = 0
    visited = [False for _ in range(len(computers))]
    for i, network in enumerate(computers) :
        if visited[i] :
            continue

        visited[i] = True
        Q = deque(get_node(network, visited))
        while Q :
            node = Q.popleft()

            visited[node] = True
            new_nodes = get_node(computers[node], visited)
            for nn in new_nodes : Q.append(nn)

        answer +=1

    return answer
