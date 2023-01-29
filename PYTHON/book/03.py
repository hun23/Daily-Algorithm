# leetcode 937
# 1. 식별자 제외 문자로그 먼저
# 2. 같은문자면 식별자순
# 3. 숫자로그는 입력순서대로
def reorderLogFiles(logs):
    """
    :type logs: List[str]
    :rtype: List[str]
    """
    letter_logs = []
    digit_logs = []
    identifiers = dict()
    for log in logs:
        log_split = log.split()
        if log_split[1].isdigit():
            digit_logs.append(log)
        else:
            value = " ".join(log_split[1:])
            letter_logs.append(value)
            if identifiers.get(value) == None:
                temp = [log_split[0]]
                identifiers[value] = temp
            else:
                identifiers[value].append(log_split[0])
    letter_logs.sort()
    for v in identifiers.values():
        v.sort()
    j = 0
    temp = ""
    for (i, log) in enumerate(letter_logs):
        if temp == log:
            j += 1
        else:
            j = 0
        letter_logs[i] = identifiers[log][j] + " " + letter_logs[i]
        temp = log
    print(letter_logs)
    print(digit_logs)
    return letter_logs + digit_logs


s = reorderLogFiles(
    [
        "dig1 8 1 5 1",
        "let1 art can",
        "dig2 3 6",
        "let2 own kit dig",
        "let3 art zero",
    ]
)

print(s)
