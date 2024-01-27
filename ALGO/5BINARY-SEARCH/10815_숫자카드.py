from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")

N = int(input())
N_arr = list(map(int, input().split()))
M = int(input())
M_arr = list(map(int, input().split()))

N_dict = dict()
for n in N_arr:
    N_dict[n] = True

for m in range(M):
    if N_dict.get(M_arr[m], False):
        print("1")
    else:
        print("0")
    if m != M - 1:
        print(" ")
