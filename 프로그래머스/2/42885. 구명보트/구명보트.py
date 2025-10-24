import heapq

def solution(people, limit):
    sorted_people = sorted(people, reverse=True)
    boat = []
    answer = 0
    for weight in sorted_people :
        if not boat :
            heapq.heappush(boat, -(limit - weight))
        else :
            last = -1 * boat[0]
            if last >= weight :
                heapq.heappop(boat)
                answer +=1
            else :
                heapq.heappush(boat, -(limit - weight))

    return len(boat)+answer
