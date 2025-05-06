from itertools import permutations

def solution(K, dungeons) :
    permu = list(permutations(dungeons, len(dungeons)))
    
    answer = 0
    for p in permu :
        current_k = K
        visit = 0
        for dungeon in p :
            if current_k >= dungeon[0] :
                current_k -= dungeon[1]
                visit +=1
        
        answer = max(answer, visit)
            
    return answer

solution(80, [[80,20],[50,40],[30,10]])