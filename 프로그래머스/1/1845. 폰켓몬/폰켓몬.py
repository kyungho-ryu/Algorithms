def solution(nums):
    answer = 0
    temp = []
    for n in nums :
        if n not in temp :
            temp.append(n)
            answer +=1

        if answer == len(nums) // 2 :
            break

    return answer


print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))
