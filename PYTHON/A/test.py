import time
from tqdm import tqdm
import random
# cores = [(i, j) for i in range(1, N-1) for j in range(1, N-1) if board[i][j] == 1]

N, M = random.randint(1000, 2000), random.randint(1000, 2000)
arr = [[random.randint(-100, 100) for _ in range(M)] for _ in range(N)]

T = 100
t1, t2, t3 = 0, 0, 0
for i in tqdm(range(T)):
    st1 = time.time()
    minuses = []
    for r in range(N):
        for c in range(M):
            if arr[r][c] < 0:
                minuses.append((r, c))
    ed1 = time.time()

    st2 = time.time()
    minuses2 = [(i, j) for i in range(N) for j in range(M) if arr[i][j] < 0]
    ed2 = time.time()

    st3 = time.time()
    minuses3 = [(0, 0)] * N * M
    idx = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c] < 0:
                minuses3[idx] = (r, c)
                idx += 1
    ed3 = time.time()

    t1 += (ed1 - st1)
    t2 += (ed2 - st2)
    t3 += (ed3 - st3)

    if not (len(minuses) == len(minuses2) == idx):
        print("ffff")
        print()
        break

print(f"for: {t1}\nlc: {t2}\nnoi: {t3}")
