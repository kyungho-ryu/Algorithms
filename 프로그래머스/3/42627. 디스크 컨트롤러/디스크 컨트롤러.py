import heapq
def solution(jobs):
    jobs.sort(key=lambda x: x[0])

    time = 0
    p_queue = []
    total_time = 0
    index = 0
    completed_works = 0
    while completed_works != len(jobs) :
        while index < len(jobs) and time >= jobs[index][0] :
            heapq.heappush(p_queue, [jobs[index][1], jobs[index][0]])
            index +=1

        if p_queue :
            hp_work = heapq.heappop(p_queue)
            consumed_time = time - hp_work[1] + hp_work[0]
            total_time += consumed_time
            time += hp_work[0]
            completed_works +=1
        else :
            time = jobs[index][0]

    return total_time//len(jobs)


print(solution([[0, 3], [1, 9], [3, 5]]))