def solution(phone_book):
    hash_table = {}
    for phone_number in phone_book:
        hash_table[phone_number] = True
    
    for phone_number in phone_book : 
        temp = ""
        for char in phone_number :
            temp +=char
            if temp in hash_table and temp != phone_number :
                return False
    

    return True