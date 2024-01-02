def make_answer(length, val, is_first, candidates):
    global answer_list, idx
    if idx > 1_000_000:
        return
    if length == 0:
        answer_list[idx] = val
        idx += 1
        return
    for digit in candidates:
        if is_first and digit == 0:
            continue
        candidates.remove(digit)
        make_answer(length - 1, val + digit * (10 ** (length - 1)), False, candidates)
        candidates.append(digit)
        candidates.sort()

answer_list = [0] * (1_000_000 + 1) 
idx = 1
for length in range(1, 10):
    make_answer(length, 0, True, [i for i in range(10)])

N = int(input())
while N != 0:
    print(answer_list[N])
    N = int(input())