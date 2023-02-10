N = int(input())
arr = list(map(int, input().split()))
arr.sort()
sum_ = 0
for i, a in enumerate(arr):
    sum_ += (len(arr) - i) * a
print(sum_)
