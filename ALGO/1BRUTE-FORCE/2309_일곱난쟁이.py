heights = [int(input()) for _ in range(9)]
heights.sort()
diff = sum(heights) - 100

for i in range(8):
    a = heights[i]
    for j in range(i + 1, 9):
        b = heights[j]
        if diff == a + b:
            heights.remove(a)
            heights.remove(b)
            for h in heights:
                print(h)
            exit()
