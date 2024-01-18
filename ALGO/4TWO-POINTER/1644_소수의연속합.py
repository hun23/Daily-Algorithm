from sys import stdin, stdout

input = stdin.readline
print = stdout.write


def println(s):
    print(f"{s}\n")


N = int(input())

is_prime = [True] * (N + 1)
is_prime[0], is_prime[1] = False, False
for i in range(int(N**0.5) + 1):
    if not is_prime[i]:
        continue
    for j in range(i * i, N + 1, i):
        is_prime[j] = False

primes = [idx for idx, yes in enumerate(is_prime) if yes]
plen = len(primes)
# 누적합 사용X
if plen == 0:
    println(0)
    exit()
ans = 0
left, right = 0, 1
temp_sum = primes[0]
# temp_sum => sum(primes[left:right])
primes.append(0)  # padding
while left < right and right < plen + 1:
    # println(f"ts: {temp_sum}, l:{left}, r:{right}")
    if temp_sum == N:
        temp_sum -= primes[left]
        temp_sum += primes[right]
        left += 1
        right += 1
        ans += 1
    elif temp_sum > N:
        temp_sum -= primes[left]
        left += 1
    elif temp_sum < N:
        temp_sum += primes[right]
        right += 1
println(ans)
# 아래는 누적합 사용
# 더 편하고(예외처리하기) 시간도 큰 차이 없다(살짝 빠르다)
# plen = len(primes)
# prefix_sum = [0] * (plen + 1)
# for i in range(1, plen + 1):
#     prefix_sum[i] = prefix_sum[i - 1] + primes[i - 1]
# # println(primes)
# # println(prefix_sum)

# ans = 0
# left, right = 0, 1
# while left < right and right < plen + 1:
#     temp_sum = prefix_sum[right] - prefix_sum[left]
#     # println(f"ts: {temp_sum}, l:{left}, r:{right}")
#     if temp_sum == N:
#         left += 1
#         right += 1
#         ans += 1
#     elif temp_sum > N:
#         left += 1
#     elif temp_sum < N:
#         right += 1
# println(ans)
