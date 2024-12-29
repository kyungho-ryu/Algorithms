def solution(prices):
    stack = []
    answer = [0 for _ in range(len(prices))]

    for i in range(len(prices)) :
        while stack and prices[stack[-1]] > prices[i] :
            idx = stack.pop()
            answer[idx] = i - idx


        stack.append(i)

    while stack :
        idx = stack.pop()
        answer[idx] = len(prices) - idx - 1

    return answer

print(solution([1, 2, 3, 2, 3])) # [4, 3, 1, 1, 0]

