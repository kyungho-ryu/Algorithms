from collections import deque
# x -> y
# 방법 3가지
# 1. x+n
# 2. x*2
# 3. x*3

# x, y, n 이 주어질 떄 최소 연산 회수 return, 없으면 -1

def solution(x, y, n) :
    queue = deque()
    queue.append([0, x]) # step, value
    visited = set({x})

    while queue :
        step, px = queue.popleft()
        if px == y:
            return step
        for action in [n, px, 2*px] :
            nx = px+action
            if nx not in visited and nx <= y:
                queue.append([step+1, nx])
                visited.add(nx)

    return -1

print(solution(10,40,5)) # 2
print(solution(10,40,30)) # 1
print(solution(2,5,4)) # -1


