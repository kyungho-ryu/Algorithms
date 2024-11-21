def solution(clothes):
    hash_table = {}
    count = 1

    for cloth, kind in clothes :
        hash_table[kind] = hash_table.get(kind, 0) + 1

    for k in hash_table.values() :
        count *= k+1

    return count -1 