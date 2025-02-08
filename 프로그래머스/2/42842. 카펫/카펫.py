def solution(B, Y) :
    temp = B / 2
    for i in range(1, int(temp//2)+1) :
        print(i)
        if Y == (temp - i - 2) * i :
            return [int(temp-i), i+2]