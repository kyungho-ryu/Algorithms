from collections import deque

def check_change(v1, v2) :
    count = 0
    for i in range(len(v1)) :
        if v1[i] != v2[i] : count +=1

    return True if count ==1 else False


def solution(begin, target, words):
    visited = {word : False for word in words}
    visited[begin] = False
    que = deque([(begin,0)])
    while que :
        item, count = que.popleft()
        visited[item] = True

        if item == target :
            return count

        for word in words :
            if check_change(item, word) and not visited[word]:
                que.append((word, count+1))

    return 0

# 제한사항
# 각 단어는 알파벳 소문자로만 이루어져 있습니다.
# 각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
# words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
# begin과 target은 같지 않습니다.
# 변환할 수 없는 경우에는 0를 return 합니다.

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])) # 4
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"])) # 0
