# leetcode 5
def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """

    def isPalindrome(s):
        return s == s[::-1]

    answer = (0, 0)
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if (j - i) > (answer[1] - answer[0]):
                if isPalindrome(s[i:j]):
                    answer = (i, j)
    if answer == (0, 0):
        return ""
    return s[answer[0] : answer[1]]
