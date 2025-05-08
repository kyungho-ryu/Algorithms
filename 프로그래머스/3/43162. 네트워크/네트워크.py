from collections import deque

def solution(n, computers) :
    visited = [False] * n
    
    count = 0 
    for j in range(n) :
        if not visited[j] :
            queue = deque()
            queue.append(j)
            visited[j] = True

            while queue :
                q = queue.popleft()
                for i, c in enumerate(computers[q]) :
                    if not visited[i] and c == 1 :
                        queue.append(i)                
                        visited[i] = True
            count += 1
            
    return count
    


solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])