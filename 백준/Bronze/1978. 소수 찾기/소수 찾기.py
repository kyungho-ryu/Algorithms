N = int(input())
_list = list(map(int, input().split()))
max_num = max(_list)

def dfs(_list, max_num) :
    is_prime = [False, False] + [True] * (max_num - 1)
    for n in range(2, int(max_num ** 0.5) + 1):
        if is_prime[n] :
            for j in range(n*n, max_num+1, n) :
                is_prime[j] = False

    return is_prime

prime_table = dfs(_list, max_num)
count =  sum(1 for num in _list if prime_table[num])
print(count)
