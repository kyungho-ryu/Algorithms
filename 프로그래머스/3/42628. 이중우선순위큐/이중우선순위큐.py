import heapq
# def solution(operations):
#     max_heap = []
#     min_heap = []
#     sync = []
#
#     while operations :
#         op = operations.pop(0)
#         if op[0] == "I" :
#             num = int(op[2:])
#             heapq.heappush(max_heap, num)
#             heapq.heappush(min_heap, num)
#         elif op == "D -1"
#             try :
#
#
#
#         exit()
#
#     return answer

def solution(operations):
    min_heap = []  # 최소 힙
    max_heap = []  # 최대 힙 (음수로 변환하여 사용)
    sync = set()   # 동기화된 값 저장 (유효한 값)

    for op in operations:
        command, value = op.split()
        value = int(value)

        if command == "I":
            # 삽입: 최소 힙과 최대 힙에 값 추가
            heapq.heappush(min_heap, value)
            heapq.heappush(max_heap, -value)
            sync.add(value)
        elif command == "D":
            if value == 1:  # 최댓값 삭제
                while max_heap  and -max_heap[0] not in sync:
                    heapq.heappop(max_heap)  # 동기화되지 않은 값 제거
                if max_heap:
                    sync.remove(-heapq.heappop(max_heap))  # 최댓값 삭제, sync에서 제거
            elif value == -1:  # 최솟값 삭제
                while min_heap  and min_heap[0] not in sync:
                    heapq.heappop(min_heap)  # 동기화되지 않은 값 제거
                if min_heap:
                    sync.remove(heapq.heappop(min_heap))  # 최솟값 삭제, sync에서 제거


    # 동기화되지 않은 값 제거
    while max_heap and -max_heap[0] not in sync:
        heapq.heappop(max_heap)
    while min_heap  and min_heap[0] not in sync:
        heapq.heappop(min_heap)

    # 결과 반환
    if not sync:
        return [0, 0]
    return [-max_heap[0], min_heap[0]]  # 최댓값, 최솟값

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]	))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]	))