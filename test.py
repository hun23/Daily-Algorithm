import sys
from pprint import pprint

sys.stdin = open("input.txt", "r")

def decode(p, patterns):
    code = ""
    for i in range(0, len(p), 7):
        tu = tuple(p[i: i + 7])
        if patterns.get(tu) is None:
            return 0
        code += str(patterns[tu])
    return code

def check(decoded):
    sum_ = 0
    for i in range(1, 8):
        if i % 2 == 0:
            sum_ += int(decoded[i - 1])
        else:
            sum_ += 3 * int(decoded[i - 1])
    if (int(decoded[-1]) + sum_) % 10 == 0:
        return sum(map(lambda x: int(x), decoded))
    else:
        return 0

def compress(bi):
    bi = bi.strip("0")
    i = 1
    while len(bi) > 56 * i:
        i += 1
    diff = 56 * i - len(bi)
    filled = ["0"] * diff
    filled.extend(bi)
    ret = []
    for i in range(0, len(filled), i):
        ret.append(int(filled[i]))
    return ret


def hex_to_bin(code):
    ret = ""
    for c in code:
        bi = str(bin(int(c, 16)))[2:]
        diff = 4 - len(bi)
        bi = "0" * diff + bi
        ret += bi
    return ret


patterns = {(0,0,0,1,1,0,1): "0", (0,0,1,1,0,0,1): "1", (0,0,1,0,0,1,1): "2",
        (0,1,1,1,1,0,1): "3", (0,1,0,0,0,1,1): "4", (0,1,1,0,0,0,1): "5",
        (0,1,0,1,1,1,1): "6", (0,1,1,1,0,1,1): "7", (0,1,1,0,1,1,1): "8",
        (0,0,0,1,0,1,1): "9"}
T = int(input())
for tc in range(1, T + 1):
    code_inputs = dict()
    N, M = map(int, input().split())
    arr = [list(input().strip()) for _ in range(N)]
    answers = []
    codes = []
    # hashing
    for r in range(N):
        temp = tuple(arr[r])
        if code_inputs.get(temp) is None:
            code_inputs[temp] = [r, r]
        else:
            code_inputs[temp][-1] = r
    # pprint(code_inputs)

    for key, value in code_inputs.items():
        # split
        key_string = "".join(key).strip("0")
        # print(f"----------------------------{tc}")
        # print(f"in: {key_string}")
        # mult = 1
        i = 1
        while True:
            before = i
            splited = key_string.split("0" * i)
            for sp in splited:
                
                if sp:
                    bi = hex_to_bin(sp)
                    bi = compress(bi)
                    decoded = decode(bi, patterns)
                    if decoded:
                        checked = check(decoded)
                        if checked:
                            answers.append(checked)
                            # print(sp, bi, checked)
                    else:
                        i += 1
                        break
            if i == before:
                break
    
    print(f"#{tc} {sum(answers)}")
    continue

    #             q, r = (56 * i - 3 * i)//4, 0 if (56 * i - 3 * i)%4==0 else 1
    #             if 0 < len(sp) < q + r:
    #                 i += 1
    #                 break
    #         if i == before:
    #             break
    #     # print(key_string)
    #     for sp in splited:
    #         if sp:
    #             codes.append(sp)
    # print(codes)
    # binaries = []
    # for code in codes:
    #     bi = hex_to_bin(code)
    #     bi = compress(bi)
    #     binaries.append(bi)
    # for b in binaries:
    #     print("".join(map(str, b)))
    # for bi in binaries:
    #     decoded = decode(bi, patterns)
    #     checked = check(decoded)
    #     if checked:
    #         answers.append((decode(bi, patterns), checked))
    # for z in zip(codes, binaries, answers):
    #     ptrn = "".join(map(str, z[1]))
    #     answ = "".join(map(str, answers))
    #     print(z[0], ptrn, answ)
    # print(f"#{tc} {sum(map(lambda x: x[1], answers))}")
    # continue