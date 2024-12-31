def solution(participant, completion):
    participants = sorted(participant)
    completions = sorted(completion)

    for i in range(len(completions)) :
        if participants[i] != completions[i] :
            return  participants[i]

    return participants[-1]


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
