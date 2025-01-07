from itertools import permutations

def is_prime(data) :
    if data < 2  :
        return False
    for i in range(2, int(data**0.5)+1) :
        if data % i == 0 :
            return False
    return True


def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        temp = permutations(numbers, i+1)
        for number in temp :
            comb = int("".join(number))
            answer.add(comb)

    prime_count = 0
    for num in answer :
        if is_prime(num) : prime_count +=1

    return prime_count


# numbers는 길이 1 이상 7 이하인 문자열입니다.
# numbers는 0~9까지 숫자만으로 이루어져 있습니다.
# "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
print(solution("17")) # 3
print(solution("011")) # 2