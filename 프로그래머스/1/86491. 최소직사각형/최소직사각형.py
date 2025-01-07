def solution(sizes):
    max_x1 = 0
    max_x2 = 0
    for n in sizes :
        x1, x2 = n
        if x1 > x2 :
            max_x1 = max(x1, max_x1)
            max_x2 = max(x2, max_x2)
        else :
            max_x1 = max(x2, max_x1)
            max_x2 = max(x1, max_x2)

    return max_x1 * max_x2