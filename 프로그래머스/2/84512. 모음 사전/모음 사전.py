def solution(word) :
    temp = ["A", "E", "I", "O", "U"]
    priority = [781, 156, 31, 6, 1]
    
    result = 0
    for i, char in enumerate(word) : 
        idx = temp.index(char)
        result += priority[i] * idx + 1
    
    return result
    
    
print(solution("AAAAE"))