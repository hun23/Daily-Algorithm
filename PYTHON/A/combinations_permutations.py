from itertools import combinations, permutations, combinations_with_replacement, product
import time
import random
from tqdm import tqdm

def comb(start_idx, cnt, arr, ret):  # faster
    if cnt == leng:
        # print(ret)
        return
    for i in range(start_idx, len(arr)):
        ret[cnt] = arr[i]
        comb(i + 1,  cnt + 1, arr, ret)
    return

def comb2(cnt, arr, ret):
    if cnt == leng:
        # print(ret)
        return
    for i in range(len(arr)):
        ret[cnt] = arr[i]
        comb2(cnt + 1, arr[i + 1:], ret)

def comb_re(start_idx, cnt, arr, ret):
    if cnt == 3:
        print(ret)
        return
    for i in range(start_idx, len(arr)):
        ret[cnt] = arr[i]
        comb_re(i,  cnt + 1, arr, ret)
    return

def permu(used, cnt, arr, ret):
    if cnt == 3:
        print(ret)
        return
    for i in range(len(arr)):
        if not used[i]:
            used[i] = True
            ret[cnt] = arr[i]
            permu(used,  cnt + 1, arr, ret)
            used[i] = False
            # ret[cnt] = 0
    return

def prod(used, cnt, arr, ret):
    if cnt == 3:
        print(ret)
        return
    for i in range(len(arr)):
        ret[cnt] = arr[i]
        prod(used,  cnt + 1, arr, ret)
    return

def bitcomb(arr):
    for i in range(1<<len(A)):
        for j in range(i)


# A = [1, 2, 3, 4]
# leng = 3
# print("my combinations")
# comb(0, 0, A, [0] * leng)
# print("my comb2")
# comb2(0, A, [0] * leng)


T = 100
t1, t2 = 0, 0
for tc in tqdm(range(T)):
    alen = random.randint(10, 22)
    A = [0] * alen
    for a in range(alen):
        A[a] = random.randint(1, 100)
    leng = random.randint(1, len(A))

    st1 = time.time()
    comb(0, 0, A, [0] * leng)
    ed1 = time.time()
    st2 = time.time()
    comb2(0, A, [0] * leng)
    ed2 = time.time()

    t1 += (ed1 - st1)
    t2 += (ed2 - st2)
print(f"t1:{t1}\nt2:{t2}")


# print("combinations")
# for c in combinations(A, 3):
#     print(c)
#
#
# print("my combinations with replacement")
# comb_re(0, 0, A, [0, 0, 0])
#
# print("comb_with_replacement")
# for c in combinations_with_replacement(A, 3):
#     print(c)
#
# print("my permutations")
# permu([False] * len(A), 0, A, [0, 0, 0])
#
# print("permutations")
# for c in permutations(A, 3):
#     print(c)
#
# print("my products")
# prod([False] * len(A), 0, A, [0] * leng)
#
# print("products")
# for c in product(A, repeat=3):
#     print(c)