# leetcode 125
def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    alnum_s = []
    for c in s:
        if c.isalnum():
            alnum_s.append(c.lower())
    alnum_s = "".join(alnum_s)
    reversed_s = "".join(reversed(alnum_s))
    for i in range(len(alnum_s)):
        if alnum_s[i] != reversed_s[i]:
            return False
    return True
