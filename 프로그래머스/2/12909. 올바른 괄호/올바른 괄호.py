def solution(s):
    temp = []

    for i, str in enumerate(s) :
        if len(temp) == 0 and str == ")" : return False
        if str == "(":
            temp.append(str)
        else :
            temp.pop()
    return len(temp) == 0

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
