def solution(number, k):
    answer = []

    for n in number :
        while answer and answer[-1] < n and k>0:
            answer.pop(-1)
            k -=1

        answer.append(n)
    return ''.join(answer)[0:len(answer)-k]

# 제한 조건
# number는 2자리 이상, 1,000,000자리 이하인 숫자입니다.
# k는 1 이상 number의 자릿수 미만인 자연수입니다.
print(solution("1924", 2)) # 94
print(solution("1231234", 3)) # 3234
print(solution("4177252841", 4)) # 775841