from itertools import permutations
def solution(k, dungeons):
    answer = 0

    permu = list(permutations(dungeons, len(dungeons)))
    for p in permu :
        current_state = k
        current_v = 0
        for data in p :
            req, consumed = data
            if current_state >= req :
                current_v +=1
                current_state -= consumed

        answer = max(answer, current_v)

    return answer