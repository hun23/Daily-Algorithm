# 내 답안
def sort_word(s):
    s = list(s)
    s.sort()
    s = str(s)
    return s

def group_anagrams(inp):
    inp_sorted = [sort_word(x) for x in inp]
    inp_sorted = set(inp_sorted)
    answer = []
    for word_sorted in inp_sorted:
        temp = []
        for word in inp:
            if sort_word(word) == word_sorted:
                temp.append(word)
        if len(temp) != 0:
            answer.append(temp)
    print(answer)


# 모범답안
def anagram(words):
    di = dict()
    for word in words:
        key = ''.join(sorted(word))
        if di.get(key) == None:
            di[key] = []
        di[key].append(word)
    print(list(di.values()))

# 본문
words = ['eat','tea','tan','ate','nat','bat']
group_anagrams(words)
anagram(words)
