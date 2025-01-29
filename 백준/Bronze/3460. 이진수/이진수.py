from collections import deque
T = int(input())
N = []
for i in range(T) :
    N.append(int(input()))

def upper_bound(n) :
    index = 0
    while True :
        if n < 2**index :
            return index
        else :
            index+=1

def solution(N) :
    for n in N :
        sum = 0
        arr = deque()
        upper_index = upper_bound(n)
        for i in range(upper_index-1,-1,-1) :
            if sum + 2**i <= n :
                sum += 2**i
                arr.appendleft(str(i))
                if sum == n :
                    print(' '.join(arr))
                    break

solution(N)
