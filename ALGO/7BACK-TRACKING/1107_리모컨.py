from sys import stdin, stdout

input = stdin.readline

def println(s):
    stdout.write(f"{s}\n")

def recur(idx, temp):
    global closest_number
    if idx > len(str(N)):
        return
    if len(temp) >= 1:
        if abs(int(temp) - N) < abs(closest_number - N):
            closest_number = int(temp)
    for a in availables:
        recur(idx + 1, temp + str(a))
    


N = int(input())
M = int(input())

if M == 0:
    print(len(str(N)))
    exit()
availables = [i for i in range(10)]
brokens = list(map(int, input().split()))
for b in brokens:
    availables.remove(b)
if N == 100:
    print(0)
    exit()
closest_number = 2147483647
recur(0, "")
print(abs(N - closest_number) + len(str(closest_number)))
# check 99 / 9 / 012345678