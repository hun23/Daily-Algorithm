def is_prime(num):
    if num <= 1:
        return False
    elif num == 2 or num == 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False

    # 5 6 7 8 9 10
    # 11 12 13 14 15 16
    for i in range(5, int(num**0.5) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True

def upside_down(num):
    pair = [0, 1, 2, -1, -1, 5, 9, -1, 8, 6]
    ret = 0
    degree = len(str(num)) - 1
    while num > 0:
        changed = pair[num%10]
        if changed == -1:
            return 0
        ret += changed * (10**degree)
        degree -= 1
        num //= 10
    return ret

N = input()
for n in list(N):
    if n in "347":
        print("no")
        break
else:
    N = int(N)
    print("yes" if is_prime(N) and is_prime(upside_down(N)) else "no")