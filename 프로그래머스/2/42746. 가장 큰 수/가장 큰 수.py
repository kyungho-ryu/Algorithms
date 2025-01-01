def solution(numbers):
    # 숫자를 문자열로 변환
    temp = [str(num) for num in numbers]
    
    # 정렬 기준: 두 문자열을 이어 붙여 비교
    temp.sort(key=lambda x: x*3, reverse=True)
    
    # 모든 숫자를 이어 붙여 결과 생성
    answer = ''.join(temp)
    
    # 0으로만 이루어진 경우 처리
    return answer if answer[0] != '0' else '0'

# 테스트
print(solution([6, 10, 2]))  # 6210
print(solution([3, 30, 34, 5, 9]))  # 9534330
print(solution([0, 0, 0]))  # 0