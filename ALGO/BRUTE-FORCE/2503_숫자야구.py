def to_abc(i):
    return (i // 100) % 10, (i // 10) % 10, i % 10

def get_strike_ball(first, second):
    strike, ball = 0, 0
    for i in range(3):
        for j in range(3):
            if first[i] == second[j]:
                if i == j:
                    strike += 1
                else:
                    ball += 1
    return strike, ball

N = int(input())
query_list = [tuple(map(int, input().split())) for _ in range(N)]

candidates = set()
for i in range(1000):
    a, b, c = to_abc(i)
    if a != 0 and b != 0 and c != 0:
        if a != b and a != c and b != c:
            candidates.add((a, b, c))

for num, strike, ball in query_list:
    to_delete = []
    for c in candidates:
        if (strike, ball) != get_strike_ball(to_abc(num), c):
            to_delete.append(c)
    for d in to_delete:
        candidates.remove(d)
print(len(candidates))
