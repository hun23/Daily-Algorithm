from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")

N = int(input())
meow = input().strip()

check = dict()
for c in "abcdefghijklmnopqrstuvwxyz":
    check[c] = 0

right = 0
while alphabet_cnt < N:
    
left, right = 0, 0
while left <= right:
    