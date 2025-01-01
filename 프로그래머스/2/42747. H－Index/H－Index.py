def solution(citations):
    # 논문의 인용 횟수를 내림차순으로 정렬
    citations.sort(reverse=True)
    
    # H-Index 계산
    for i in range(len(citations)):
        # i번째 논문까지는 인용 횟수가 (i+1)번 이상인지 확인
        if citations[i] < i + 1:
            return i
    
    # 모든 논문이 조건을 만족하면 전체 논문 수를 반환
    return len(citations)

# 테스트
print(solution([3, 0, 6, 1, 5]))  # 3
print(solution([10, 8, 5, 4, 3]))  # 4
print(solution([25, 8, 5, 3, 3]))  # 3
print(solution([0, 0, 0, 0]))      # 0