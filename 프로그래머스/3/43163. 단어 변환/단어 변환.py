from collections import deque
# begin에서 target으로 변환하는 가장 짧은 변환
# 1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
# 2. words에 있는 단어로만 변환할 수 있습니다.

# 예를 들어 begin이 "hit", target가 "cog"
# words가 ["hot","dot","dog","lot","log","cog"]라면
# "hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환할 수 있습니다.

# 단어 길이: 3~10
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log"]	 # 3개 이상 50개 이하

# 500
# 490
# 480
# 1
def solution(begin, target, words) :
    set_words = set(words)

    # 변환할 수없으면 0 return
    if target not in set_words : return 0

    length = len(target)

    candidates = [[] for _ in range(length)]
    for word in words :
        for i, w in enumerate(word) :
            if w not in candidates[i] :
                candidates[i].append(w)

    queue = deque()
    queue.append([0, begin])
    visited = set()
    visited.add(begin)

    while queue :
        num, c_word = queue.popleft()
        if c_word == target :
            return num

        for i in range(length) :
            for candiate in candidates[i] :
                if candiate != c_word[i] :
                    n_word = c_word[0:i] + candiate + c_word[i+1:length]
                    if n_word not in visited and n_word in set_words:
                        queue.append([num+1, n_word])
                        visited.add(n_word)
    return -1

print(solution(begin, target, words))