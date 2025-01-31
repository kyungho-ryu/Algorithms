def solution(brown, yellow):
    total_tiles = brown + yellow

    for i in range(3, int(total_tiles**0.5)+1) :
        if total_tiles % i == 0 :
            j = total_tiles // i
            if yellow == (i-2) * (j-2) :
                return [j, i]
    return []

# 제한사항
# 갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
# 노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
# 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.

print(solution(10, 2)) # [4,3]
print(solution(8, 1)) # [3,3]
print(solution(24, 24)) # [8,6]
