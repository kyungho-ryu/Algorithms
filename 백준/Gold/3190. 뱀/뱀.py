from collections import deque

N = int(input())
K = int(input())
apples = []
for _ in range(K) :
    apples.append(list(map(int, input().split())))

L = int(input())
moves = deque()
for _ in range(L) :
    moves.append(list(input().split()))
moves.append(('10000','-'))

answer = 0

body = deque()
body.append((0, 0))
d_index = 0
directs = [[0,1],[1,0],[0,-1],[-1,0]]
finished = False

def check_finished(body, pos, N) :
    if 0 <= pos[0] < N and 0 <= pos[1] < N and pos not in body :
        return False
    return True

def change_direction(d_index) :
    if c_d == "D":
        if d_index + 1 == len(directs):
            temp = 0
        else:
            temp = d_index+1
    else:
        if d_index - 1 < 0:
            temp = 3
        else:
            temp = d_index-1

    return temp

while moves :
    t, c_d = moves.popleft()
    for i in range(int(t)-answer) :
        current_pos = body[-1]

        pos = [current_pos[0] + directs[d_index][0], current_pos[1] + directs[d_index][1]]
        answer +=1
        if check_finished(body, pos, N) :
            finished = True
            break

        body.append(pos)
        if [pos[0] + 1, pos[1] + 1] in apples:
            apples.remove([pos[0] + 1, pos[1] + 1])  # 사과 먹으면 꼬리 유지
        else:
            body.popleft()  # 사과 없으면 꼬리 제거
        
    if finished :
        break

    d_index = change_direction(d_index)

print(answer)
