def solution(answers):
    h1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5] * 1000
    h2 = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5] * 1000
    h3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    correct_number = [0,0,0]
    for i in range(len(answers)) :
        if answers[i] == h1[i] :
            correct_number[0] +=1
        if answers[i] == h2[i] :
            correct_number[1] +=1
        if answers[i] == h3[i] :
            correct_number[2] +=1

    max = 0
    answer = []
    for i in range(len(correct_number)) :
        if correct_number[i] > max :
            answer = [i+1]
            max = correct_number[i]
        elif correct_number[i] == max :
            answer.append(i+1)

    return answer


# 시험은 최대 10,000 문제로 구성되어있습니다.
# 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
print(solution([1,2,3,4,5])) # [1]
print(solution([1,3,2,4,2])) # [1,2,3]