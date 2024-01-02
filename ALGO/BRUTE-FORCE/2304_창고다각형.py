def get_x_length(pillar_list, height):
    left, right = 0, len(pillar_list) - 1
    left_found = pillar_list[left][1] >= height
    right_found = pillar_list[right][1] >= height
    while not (left_found and right_found):
        if not left_found:
            left += 1
            left_found = pillar_list[left][1] >= height
        if not right_found:
            right -= 1
            right_found = pillar_list[right][1] >= height
    return pillar_list[right][0] - pillar_list[left][0] + 1

N = int(input())
pillar_list = [tuple(map(int, input().split())) for _ in range(N)]
pillar_list.sort()
max_height = sorted(pillar_list, key=lambda x:x[1])[-1][1]

ans = 0
for height in range(1, max_height + 1):
    ans += get_x_length(pillar_list, height)
print(ans)
