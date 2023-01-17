import copy

m, n = map(int, input().split())
arr = list(range(2, n + 1))
# mine 78004kb 7760ms
# prime = [2]
# temp = []
# while (prime[-1]**2 <= n):
#     for i in arr:
#         if i % prime[-1] != 0:
#             temp.append(i)
#     arr = copy.deepcopy(temp)
#     temp.clear()
#     prime.append(arr[0])
# prime += arr[1:]
# for p in prime:
#     if m <= p <= n:
#         print(p)

# from internet 79252kb 408ms
is_prime_arr = [True for _ in range(n + 1)]
is_prime_arr[0] = False
is_prime_arr[1] = False
for i in range(2, n + 1):
    if i ** 2 > n:
        break
    if is_prime_arr[i] == True:
        for j in range(i + i, n + 1, i):
            is_prime_arr[j] = False
for (i, p) in enumerate(is_prime_arr):
    if p and i >= m:
        print(i)