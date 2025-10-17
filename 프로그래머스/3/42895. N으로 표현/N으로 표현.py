# 예제
# 5와 사칙연산 만으로 12를 표현
# 12 = 5 + 5 + (5 / 5) + (5 / 5)
# 12 = 55 / 5 + 5 / 5
# 12 = (55 + 5) / 5

# N, number가 주어질 떄, N과 사칙연산만 사용해서 표현할 수 있는 방법 중 최소값을 return
# 나누기에서 나머지는 무시
# 최소값이 8보다 크면 -1 retrun
def solution(N, number) :
    DP = [set() for _ in range(8)]
    for i in range(8) :
        DP[i].add(int(str(N)*(i+1)))
        for j in range(i) :
            for x in DP[j] :
                for y in DP[i-j-1] :
                    DP[i].add(x+y)
                    DP[i].add(x-y)
                    DP[i].add(x*y)
                    if y!= 0 :
                        DP[i].add(x//y)

        if number in DP[i] :
            return i+1
    return -1

N = 5 # 1~9
number = 12 # 1~32,000
print(solution(N, number)) # 4
