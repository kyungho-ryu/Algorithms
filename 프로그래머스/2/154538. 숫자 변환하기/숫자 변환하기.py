from collections import deque

def solution(x, y, n):
    queue = deque([[x, 0]])
    visited = set([x])
    
    while queue :
        s, count = queue.popleft()
        if s == y : 
            return count
        
        if s + n <= y and s + n not in visited:
            queue.append([s+n, count+1])
            visited.add(s+n)
        if s * 2 <= y and s * 2 not in visited:
            queue.append([s*2, count+1])
            visited.add(s*2)
        if s * 3 <= y and s * 3 not in visited:
            queue.append([s*3, count+1])
            visited.add(s*3)
    return -1


solution(10, 40, 5)