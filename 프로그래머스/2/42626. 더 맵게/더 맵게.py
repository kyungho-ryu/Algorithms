import heapq

def solution(scoville, K):
    answer = 0
    temp = scoville.copy()
    heapq.heapify(temp)
    while temp :
        s1 = heapq.heappop(temp)
        if s1 < K:
            if temp :
                s2 = heapq.heappop(temp)
                heapq.heappush(temp, s1 + 2*s2)
                answer +=1
        else :
            heapq.heappush(temp, s1)
            break

    if temp : return answer
    else : return -1

print(solution([1, 2, 3, 9, 10, 12], 7))