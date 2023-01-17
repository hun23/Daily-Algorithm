words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

temp = ""
for (i, w) in enumerate(words):
    if i == 0:
        temp = w
        continue
    if w == "done":
        break
    if temp[-1] != w[0] or temp == w:
        print(f"{i} just failed")
    temp = w
    