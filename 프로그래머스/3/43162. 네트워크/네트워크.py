def solution(n, computers):
    answer = 0
    dict_data = {i: computers[i] for i in range(len(computers))}
    visited = [False] * len(computers)
    while dict_data :
        stack = [[list(dict_data.keys())[0], dict_data.pop(list(dict_data.keys())[0])]]
        while stack :
            index, link = stack.pop()
            for i in range(len(link)):
                if link[i] == 1 and i in dict_data.keys():
                    stack.append([i, dict_data.pop(i)])

        answer +=1

    return answer