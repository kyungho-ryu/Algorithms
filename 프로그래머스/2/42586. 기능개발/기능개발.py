import math


def solution(progresses, speeds):
    if len(progresses) == 0:
        return []

    answer = []
    total_time = 0
    completed_works = 1

    for p, s in zip(progresses, speeds):
        time = math.ceil((100 - p) /s)
        if time > total_time:
            if total_time != 0:
                answer.append(completed_works)
                completed_works = 1

            used_time = time - total_time
            total_time += used_time

        else:
            completed_works += 1

    answer.append(completed_works)

    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progresses, speeds))