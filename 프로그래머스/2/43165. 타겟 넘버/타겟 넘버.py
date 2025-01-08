def solution(numbers, target):
    def dfs(index, sum) :
        if index == len(numbers):
            return 1 if sum == target else 0

        return dfs(index+1, sum+numbers[index]) + dfs(index+1, sum-numbers[index])

    return dfs(0, 0)


print(solution([1, 1, 1, 1, 1], 3))  # 5
print(solution([4, 1, 2, 1], 4))  # 2
