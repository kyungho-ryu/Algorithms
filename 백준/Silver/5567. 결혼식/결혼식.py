N = int(input())
M = int(input())
relations = [list(map(int, input().split())) for _ in range(M)]

def solution(N, M, relations):
    key = set()
    visited = set()
    key.add(1)
    visited.add(1)
    count = 0

    for _ in range(2):  # 친구, 친구의 친구까지
        new_key = set()
        for a, b in relations:
            if a in key and b not in visited:
                new_key.add(b)
                visited.add(b)
                count += 1
            elif b in key and a not in visited:
                new_key.add(a)
                visited.add(a)
                count += 1
        key = new_key

    print(count)

solution(N, M, relations)