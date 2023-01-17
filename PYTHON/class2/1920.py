import sys

n = int(input())
n_arr = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())
m_arr = list(map(int, sys.stdin.readline().rstrip().split()))

# used "in"
# for i in range(len(m_arr)):
#     if m_arr[i] in n_arr:
#         print(1)
#     else:
#         print(0)

# used "binary search"
n_arr.sort()
# print(n_arr)
for m_num in m_arr:
    lo = 0
    hi = len(n_arr) - 1
    found = 0
    # print(f"lo:{n_arr[lo]} hi:{n_arr[hi]}")
    # print(m_num)
    if n_arr[lo] == m_num or n_arr[hi] == m_num:
        found = 1
    else:
        while lo + 1 < hi:
            mid = int((lo + hi) / 2)
            # print(f"lo={lo} hi={hi}")
            # print(f"mid:{n_arr[mid]}")
            if m_num < n_arr[mid]:
                hi = mid
            elif n_arr[mid] < m_num:
                lo = mid
            else:
                found = 1
                break
    print(1 if found else 0)
