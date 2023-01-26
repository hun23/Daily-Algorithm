import sys

n, m = map(int, input().split())
n_set = set()
m_set = set()
for _ in range(n):
    n_set.add(sys.stdin.readline().rstrip())
for _ in range(m):
    m_set.add(sys.stdin.readline().rstrip())
uni = list(n_set.intersection(m_set))
uni.sort()
print(len(uni))
for name in uni:
    print(name)
