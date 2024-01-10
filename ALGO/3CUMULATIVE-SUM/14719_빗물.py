from sys import stdin, stdout
input = stdin.readline
print = stdout.write

def println(s):
    print(f"{s}\n")

H, W = map(int, input().split())
heights = list(map(int, input().split()))

for h in heights:
    