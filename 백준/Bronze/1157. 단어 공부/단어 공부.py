strings = input()

def solution(strings) :


    hashmap = {}
    max = 0
    max_char = []
    for s in strings :
        key = s if ord(s) <= 90 else chr(ord(s) - 32)
        hashmap[key] = hashmap.get(key, 0) + 1

        if hashmap[key] > max :
            max = hashmap[key]
            max_char = [key]
        elif hashmap[key] == max :
            max_char.append(key)


    return max_char[0] if len(max_char) == 1 else "?"

print(solution(strings))