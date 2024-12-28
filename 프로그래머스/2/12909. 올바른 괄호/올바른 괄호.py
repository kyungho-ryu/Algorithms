def solution(s):
    temp = []

    for i, str in enumerate(s) :
        if str == "(":
            temp.append(str)
        else :
            try:
                temp.pop()
            except :
                return False
    return len(temp) == 0

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
