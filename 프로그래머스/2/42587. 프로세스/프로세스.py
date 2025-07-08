from collections import deque

def solution(priorities, location):
    answer = 0
    sorted_priorities = sorted(priorities)
    queue = deque(i for i in range(len(priorities)))
    
    while queue :
        value = queue.popleft()
        
        if sorted_priorities[-1] == priorities[value] :
            answer += 1
            sorted_priorities.pop(-1)
            if value == location: break
        else :
            queue.append(value)
    
    return answer