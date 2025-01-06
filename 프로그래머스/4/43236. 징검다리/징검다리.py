def solution(distance, rocks, n):
    left, right = 1, distance
    answer = 0
    rocks.append(distance)
    rocks.sort()

    while left <= right :
        mid = (left + right) // 2
        current = 0
        removed = 0

        for rock in rocks :
            if rock - current < mid :
                removed +=1
            else :
                current = rock

        if removed <= n :
            answer = mid
            left = mid +1
        else :
            right = mid -1 

    return answer

#제한사항
#도착지점까지의 거리 distance는 1 이상 1,000,000,000 이하입니다.
#바위는 1개 이상 50,000개 이하가 있습니다.
#n 은 1 이상 바위의 개수 이하입니다.
print(solution(25,[2, 14, 11, 21, 17],2)) # 4

