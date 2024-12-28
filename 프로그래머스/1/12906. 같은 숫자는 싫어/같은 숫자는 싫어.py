from collections import deque


def solution(arr):
    if len(arr) == 0 :
        return []
    
    result = [arr[0]]

    for i in range(1, len(arr)) :
        if result[-1] != arr[i] :
            result.append(arr[i])

    return result 

test_data = [1, 1, 3, 3, 0, 1, 1]
print(solution(test_data))
