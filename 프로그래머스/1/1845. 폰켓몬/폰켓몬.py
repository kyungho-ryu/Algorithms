def solution(nums):
    answer = 0    
    max = int(len(nums)/2) 
    result = []
    
    if len(nums) % 2 != 0 : return null
    else :
        for i in nums :
            if i not in result : 
                result.append(i)
        
        answer =  max if len(result) >= max else len(result)
        
        return answer