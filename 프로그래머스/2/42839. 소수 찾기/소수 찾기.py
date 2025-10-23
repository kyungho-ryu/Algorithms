from itertools import permutations, combinations
import math
def check_sosu(n) :
    if n == 0 or n == 1: 
        return False
    elif n == 2:
        return True
    else :
        for i in range(2, int(n**0.5)+1) :
            if n % i == 0 and n != i:
                return False

        return True
            
    
# 만들 수 있는 소수가 몇 개인지 return
def solution(number):
    answer = set()
    list_number = [n for n in number]
    
    for i in range(1, len(number)+1) :
        if i == 1 :
            for n in list_number :
                if check_sosu(int(n)) : answer.add(int(n)) 
        else :
            pm = list(permutations(list_number, i))
            for n in pm :
                temp = ""
                for i, char in enumerate(n) :
                    if i == 0 and char == '0' : 
                        continue
                    else :
                        temp += char
                if check_sosu(int(temp)) : answer.add(int(temp)) 
    
    return len(answer)

# 1이상 7이하 문자열, 0~9까지 숫자
# #  17 -> [7, 17, 71]
# number = "17" 

# print(solution(number))