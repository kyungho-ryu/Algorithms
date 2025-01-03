def solution(name):
    # 알파벳을 변경하는 최소 횟수 계산
    def change_count(char):
        return min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
    
    # 알파벳 변경 횟수 계산
    moves = sum(change_count(char) for char in name)
    
    # 좌우 이동 최소 횟수 계산
    n = len(name)
    min_move = n - 1
    for i in range(n):
        next_idx = i + 1
        # 연속된 A를 찾음
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
        # 왼쪽으로 갔다가 오른쪽으로 돌아오는 경우
        min_move = min(min_move, i + 2 * (n - next_idx))
        # 오른쪽으로 갔다가 왼쪽으로 돌아오는 경우
        min_move = min(min_move, 2 * i + n - next_idx)
    
    return moves + min_move