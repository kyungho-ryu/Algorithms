def solution(numbers, target) :
    def dfs(i, sum) :
        answer = 0
        if i == len(numbers) :
            if target == sum :
                return 1
            else :
                return 0

        for sym in [-1, 1] :
            v = numbers[i] * sym
            answer += dfs(i+1, v+sum)

        return answer

    return dfs(0, 0)

print(solution([4,1,2,1]	, 2))