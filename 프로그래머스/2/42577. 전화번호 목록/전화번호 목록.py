

def solution(phonebooks) :
    hashmap = {}
    for phone in phonebooks :
        hashmap[phone] = True

    for phone in phonebooks :
        temp = ""
        for char in phone :
            temp += char
            if temp in hashmap and temp != phone : return False

    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))