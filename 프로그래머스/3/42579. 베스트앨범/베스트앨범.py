import heapq

def solution(genres, plays):
    answer = []
    hash_map = {}
    popular_genres = []

    index = 0
    for g, p in zip(genres, plays) :
        if g not in hash_map :
            hash_map[g] = [[], 0]

        heapq.heappush(hash_map[g][0], (-p, index))
        hash_map[g][1] += -p
        index +=1
    print(hash_map)

    for k, v in hash_map.items() :
        heapq.heappush(popular_genres, [v[1], k])
    print(popular_genres)

    for i in range(len(hash_map.keys())) :
        p, g = heapq.heappop(popular_genres)
        for j in range(min(2, len(hash_map[g][0]))) :
            answer.append(heapq.heappop(hash_map[g][0])[1])
            
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

