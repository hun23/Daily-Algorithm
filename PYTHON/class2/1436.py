def doom(i):
    s = str(i)
    doom_count = 0
    for c in s:
        if c == '6':
            doom_count += 1
        else:
            doom_count = 0
        if doom_count >= 3:
            return True
    return False

n = int(input())
count = 0
i = 0
while True:
    i += 1
    if doom(i):
        count += 1
        if count == n:
            print(i)
            break