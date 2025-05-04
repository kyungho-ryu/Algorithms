

def solution(participants, completions) :
    participants.sort()
    completions.sort()

    for p, c in zip(participants, completions) :
        if p != c :
            return p

    return participants[-1]

print(solution(["leo", "kiki", "eden"]	, ["eden", "kiki"]	))