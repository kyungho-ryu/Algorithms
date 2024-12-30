import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    entry_finder = {}
    counter = 0

    for operation in operations:
        command, num = operation.split()
        num = int(num)

        if command == 'I':
            heapq.heappush(min_heap, (num, counter))
            heapq.heappush(max_heap, (-num, counter))
            entry_finder[counter] = num
            counter += 1
        elif command == 'D':
            if num == 1 and max_heap:
                while max_heap and max_heap[0][1] not in entry_finder:
                    heapq.heappop(max_heap)
                if max_heap:
                    _, idx = heapq.heappop(max_heap)
                    del entry_finder[idx]
            elif num == -1 and min_heap:
                while min_heap and min_heap[0][1] not in entry_finder:
                    heapq.heappop(min_heap)
                if min_heap:
                    _, idx = heapq.heappop(min_heap)
                    del entry_finder[idx]

    while min_heap and min_heap[0][1] not in entry_finder:
        heapq.heappop(min_heap)
    while max_heap and max_heap[0][1] not in entry_finder:
        heapq.heappop(max_heap)

    if not entry_finder:
        return [0, 0]
    else:
        min_val = min_heap[0][0]
        max_val = -max_heap[0][0]
        return [max_val, min_val]
