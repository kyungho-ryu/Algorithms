from itertools import combinations

n = int(input())
_list = list(map(int, input().split()))
x = int(input())

def solution(n, _list, x) :
    _list.sort()

    left, right = 0, len(_list)-1
    result = 0
    while left < right :
        temp = _list[left] + _list[right]
        if x < temp :
            right -=1
        elif x == temp :
            left +=1
            right -=1
            result +=1
        else :
            left +=1

    return result

print(solution(n, _list, x))