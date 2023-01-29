# leetcode 49

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
di = dict()
for word in strs:
    sorted_word = "".join(sorted(word))
    if di.get(sorted_word) == None:
        di[sorted_word] = [word]
    else:
        di[sorted_word].append(word)
print([x for x in di.values()])
