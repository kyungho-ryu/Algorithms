def solution(numbers, target) :
    def dfs (index, _sum) :
        if index == len(numbers) :
            return 1 if _sum == target else 0 
        
        return dfs(index+1, _sum + numbers[index]) + dfs(index + 1 , _sum - numbers[index])
    
    return dfs(0, 0)
        
    
print(solution([1,1,1,1,1], 3))