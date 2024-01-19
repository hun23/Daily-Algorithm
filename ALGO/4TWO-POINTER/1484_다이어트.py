from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")


G = int(input())
# G = A**2 - B**2
A, B = int(G**0.5) + 1, 1
ans = []
while A > B:
    temp = A**2 - B**2
    # println(f"{A}, {B}, {temp}")
    if temp < G:
        A += 1
    elif temp > G:
        B += 1
    else:
        ans.append(A)
        A += 1
        B += 1
if len(ans) == 0:
    println("-1")
else:
    for a in ans:
        println(a)
