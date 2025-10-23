# return: k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자
def solution(number, k):
    stack = []
    _k = k
    for n in number:
        while stack and _k > 0 and stack[-1] < n:
            stack.pop(-1)
            _k -=1
        stack.append(n)

    for i in range(_k) :
        stack.pop(-1)

    return ''.join(stack)