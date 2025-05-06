import math 

def solution(k, d):
    answer = 0
    
    for x in range(0, d+1, k) :
        max_y = math.floor((d*d - x*x)**0.5)
        answer += (max_y // k) +1
    
    return answer
