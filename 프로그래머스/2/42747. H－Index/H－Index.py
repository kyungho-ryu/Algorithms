def solution(citations):
    temp = sorted(citations, reverse=True)

    for i in range(len(temp)) :
        if i+1 > temp[i] : return  i

    return len(citations)
# 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
# 논문별 인용 횟수는 0회 이상 10,000회 이하입니다.
print(solution([5,5,5,100, 1]))

