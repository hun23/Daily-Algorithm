from sys import stdin, stdout
input = stdin.readline
print = stdout.write

T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    
    # k소인수분해
    divided = dict()
    for i in range(2, int(k**0.5) + 1):
        while k % i == 0:
            divided[i] = divided.get(i, 0) + 1
            k //= i
    if k != 1:
        divided[k] = 1
    print(f"divided: {divided}\n")
    
    # 각 소인수가 몇개까지 되는지 판단
    ans = 1_000_000_000_000_000_000
    for key, val in divided.items():
        print(f"key:{key}, val:{val}\n")
        cnt = 0
        div = key
        while div <= n:
            cnt += n // div
            print(f"{div} {cnt} \n")
            div *= key
        ans = min(ans, cnt//val)
    print(f"{ans}\n")
