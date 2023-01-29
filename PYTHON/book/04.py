# leetcode 819
def mostCommonWord(paragraph, banned):
    """
    :type paragraph: str
    :type banned: List[str]
    :rtype: str
    """
    count = dict()
    not_a_word = "!?',;."
    for c in not_a_word:
        paragraph = paragraph.replace(c, " ")
    words = paragraph.lower().split()
    for word in words:
        if word not in banned:
            if count.get(word) == None:
                count[word] = 1
            else:
                count[word] += 1
    return sorted(count.items(), key=lambda x: x[1], reverse=True)[0][
        0
    ]
