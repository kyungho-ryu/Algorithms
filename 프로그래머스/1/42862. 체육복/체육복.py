def solution(n, lost, reserve):
    lost_arr = set(lost) - set(reserve)
    reserve_arr = set(reserve) - set(lost)

    for i in reserve_arr :

        if i-1 in lost_arr :
            lost_arr.remove(i-1)
        elif i+1 in lost_arr :
            lost_arr.remove(i+1)

    return n - len(lost_arr)

print(solution(5, [2,4], [1,3,5]))
print(solution(5, [2,4], [3]))
print(solution(3, [2,4], [3,4]))

