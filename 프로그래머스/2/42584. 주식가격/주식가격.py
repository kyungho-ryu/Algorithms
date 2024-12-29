from collections import deque

def solution(prices):
    temp = deque(prices)
    answer = []

    while temp :
        price = temp.popleft()
        decreased = False
        for i, p in enumerate(temp) :
            if price > p :
                answer.append(i+1)
                decreased = True
                break

        if not decreased :
            answer.append(len(temp))
    return answer

print(solution([1, 2, 3, 2, 3])) # [4, 3, 1, 1, 0]

