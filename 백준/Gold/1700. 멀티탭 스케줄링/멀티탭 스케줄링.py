N, K = map(int, input().split())
items = list(map(int, input().split()))

def solution(N, K, items):
    result = 0
    memory = set()
    
    for i in range(K):
        # 이미 꽂혀 있는 경우 패스
        if items[i] in memory:
            continue

        # 공간이 남아있으면 바로 꽂음
        if len(memory) < N:
            memory.add(items[i])
        else:
            # 가장 나중에 다시 사용될 플러그를 찾아 제거해야 함
            last_used = {}
            
            for item in memory:
                try:
                    last_used[item] = items[i:].index(item)
                except ValueError:
                    last_used[item] = float('inf')  # 앞으로 사용되지 않음
            
            # 가장 나중에 사용될 플러그를 찾음
            to_remove = max(last_used, key=last_used.get)
            memory.remove(to_remove)
            
            # 새로운 아이템을 추가
            memory.add(items[i])
            result += 1

    return result

print(solution(N, K, items))