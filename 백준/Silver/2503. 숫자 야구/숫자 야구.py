from itertools import permutations


def count_strike_ball(guess, target):
    strike = sum(g == t for g, t in zip(guess, target))
    ball = len(set(guess) & set(target)) - strike
    return strike, ball


def is_valid_candidate(candidate, questions):
    for q_num, q_strike, q_ball in questions:
        strike, ball = count_strike_ball(candidate, q_num)
        if strike != q_strike or ball != q_ball:
            return False
    return True


def main():
    N = int(input())
    questions = []
    for _ in range(N):
        num, s, b = input().split()
        questions.append((num, int(s), int(b)))

    digits = '123456789'
    candidates = [''.join(p) for p in permutations(digits, 3)]

    valid_count = 0
    for cand in candidates:
        if is_valid_candidate(cand, questions):
            valid_count += 1

    print(valid_count)


if __name__ == "__main__":
    main()
