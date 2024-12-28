
def solution(progresses, speeds):
    answer = []
    for p, s in zip(progresses, speeds) :
        used_time = -((p - 100) // s)
        if len(answer) == 0 or answer[-1][1] < used_time:
            answer.append([1, used_time])
        else :
            answer[-1][0] += 1

    return [v[0] for v in answer]



progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))