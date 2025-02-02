
def dfs(index, N, n, add, sub, mul, div) :
    global max_v, min_v
    if index == len(N) :
        max_v = max(max_v, n)
        min_v = min(min_v, n)
        return

    if add >0 :
        dfs(index+1, N, n+N[index], add-1, sub, mul, div)
    if sub >0 :
        dfs(index+1, N, n-N[index], add, sub-1, mul, div)
    if mul >0 :
        dfs(index+1, N, n*N[index], add, sub, mul-1, div)
    if div >0 :
        if n < 0:
            dfs(index+1, N, -(-n//N[index]), add, sub, mul, div-1)
        else :
            dfs(index+1, N, n//N[index], add, sub, mul, div-1)

T = int(input())
N = list(map(int, input().split(' ')))
C = list(map(int, input().split(' ')))

max_v = -int(1e9)
min_v = int(1e9)

dfs(1, N, N[0], C[0], C[1], C[2], C[3])

print(max_v)
print(min_v)
