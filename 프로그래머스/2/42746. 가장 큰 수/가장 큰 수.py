def solution(numbers):
    answer = ''

    temp = [str(num) for num in numbers]
    temp = sorted(temp, key=lambda x:x*3, reverse=True)
    answer = ''.join(temp)
    return answer if answer[0] !="0" else '0'

# numbers의 원소는 0 이상 1,000 이하입니다.
print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([0,0,0]))