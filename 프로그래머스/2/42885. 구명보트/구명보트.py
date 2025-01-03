def solution(people, limit):
    answer = 0
    people.sort()
    left, right = 0, len(people)-1

    while left <= right :
        if people[right] + people[left] <= limit :
            left +=1
        answer +=1
        right -=1
    return answer


# 제한사항
# 무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
# 각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
# 구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
# 구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.
print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
