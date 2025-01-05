def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    pivot = -30001
    for route in routes :
        if pivot < route[0] :
            pivot = route[1]
            answer +=1

    return answer
