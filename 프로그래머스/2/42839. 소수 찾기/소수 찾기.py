from itertools import permutations

def cal_func(data) :
    for i in range(len(data)) :
        if data[i] != 0 :
            data = int(data[i:])
            break

    if data == 0 or data ==1 :
        return 0
    for i in range(2, data) :
        if data % i == 0 :
            return 0

    return data


def solution(numbers):
    answer = set()

    for i in range(len(numbers)):
        temp = set(permutations(numbers, i+1))

        for number in temp :
            comb = "".join(number)
            answer.add(cal_func(comb))
    return len(answer) - 1


# numbers는 길이 1 이상 7 이하인 문자열입니다.
# numbers는 0~9까지 숫자만으로 이루어져 있습니다.
# "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
print(solution("17")) # 3
print(solution("011")) # 2
