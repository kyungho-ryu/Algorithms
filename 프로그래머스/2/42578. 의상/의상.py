def solution(clothes):
    hash_map = {}
    count = 1
    for name, key in clothes :
        hash_map[key] = hash_map.get(key, 0) +1

    for value in hash_map.values() :
        count *= value+1


    return count-1



print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))

