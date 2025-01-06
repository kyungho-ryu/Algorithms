def solution(n, times):
    left, right = 1, max(times) * n
    answer = right

    while left <= right :
        mid = (left + right) // 2
        m = 0

        for t in times :
            m += mid // t

        if m >= n :
            answer = mid
            right = mid-1
        else :
            left = mid + 1

    return answer

#제한사항
#입국심사를 기다리는 사람은 1명 이상 1,000,000,000명 이하입니다.
#각 심사관이 한 명을 심사하는데 걸리는 시간은 1분 이상 1,000,000,000분 이하입니다.
#심사관은 1명 이상 100,000명 이하입니다.
print(solution(6, [7, 10])) # 28


