from collections import deque

def solution(bridge_length, weight, truck_weights):
    cumulative_time = 0
    cumulative_weight = 0
    pending_trucks = deque(truck_weights)
    processing_trucks = deque()

    while pending_trucks or processing_trucks :
        if processing_trucks and bridge_length == cumulative_time - processing_trucks[0][1] :
            truck = processing_trucks.popleft()
            cumulative_weight -= truck[0]

        if pending_trucks:
            w = pending_trucks[0]
            if cumulative_weight + w <= weight:
                cumulative_weight += w
                processing_trucks.append([w, cumulative_time])
                pending_trucks.popleft()

        cumulative_time +=1

    return cumulative_time



print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
