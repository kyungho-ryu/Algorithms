from collections import deque

def solution(priorities, location):
    cumulative_works = 0
    temp = deque([p, i]for i, p in enumerate(priorities))

    while len(temp) >= 0 :
        current_work = temp.popleft()
        if any(current_work[0] < work[0] for work in temp) :
            temp.append(current_work)
        else :
            cumulative_works +=1
            if current_work[1] == location :
                return cumulative_works


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))