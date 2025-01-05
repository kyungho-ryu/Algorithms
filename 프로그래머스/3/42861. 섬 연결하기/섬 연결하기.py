def find_root(parents, x) :
    if parents[x] != x :
        return find_root(parents, parents[x])
    return parents[x]

def union(parent, rank, x, y) :
    root_x = find_root(parent, x)
    root_y = find_root(parent, y)

    if root_x != root_y :
        if rank[root_x] > rank[root_y] :
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y] :
            parent[root_x] = root_y
        else :
            parent[root_y] = root_x
            rank[root_x] +=1

def solution(n, costs):
    answer = 0
    parents = [i for i in range(n)]
    rank = [0 for i in range(n)]
    costs.sort(key=lambda x:x[2])
    for v in costs :
        node_i, node_j, cost = v

        if find_root(parents, node_i) != find_root(parents, node_j) :
            union(parents, rank, node_i, node_j)
            answer += cost

    return answer

# 섬의 개수 n은 1 이상 100 이하입니다.
# costs의 길이는 ((n-1) * n) / 2이하입니다.
# 임의의 i에 대해, costs[i][0] 와 costs[i] [1]에는 다리가 연결되는 두 섬의 번호가 들어있고, costs[i] [2]에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용입니다.
# 같은 연결은 두 번 주어지지 않습니다. 또한 순서가 바뀌더라도 같은 연결로 봅니다. 즉 0과 1 사이를 연결하는 비용이 주어졌을 때, 1과 0의 비용이 주어지지 않습니다.
# 모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.
# 연결할 수 없는 섬은 주어지지 않습니다.
print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])) # 4
