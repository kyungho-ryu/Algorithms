def solution(phone_book):
    hash_table = {}
    for num in phone_book:
        hash_table[num] = True

    for num in phone_book :
        temp = ""
        for char in num :
            temp +=char
            if temp in hash_table.keys() and temp != num :
                return False
    return True


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))
