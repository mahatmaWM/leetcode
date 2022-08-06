from aem import con
from torch import le


def reverseWords(s):
    # write code here
    #         去掉字符串首位的空格，简化问题
    s = s.lstrip(" ")
    s = s.rstrip(" ")
    s = list(s)
    # print(s)
    #         反转一个字符串
    def helper(s, left, right):
        #             n = len(s)
        #             left, right = 0, n-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left +=1
            right -=1
        return

    #         i, j = 0, len(s)-1
    helper(s, 0, len(s) - 1)
    # print(s)
    left, right = 0, 0
    while right < len(s):
        #             找到一个单词了
        if s[right] == " " and s[left] != " ":
            helper(s, left, right - 1)
            left = right
            right += 1
        elif s[right] == " " and s[left] == " ":
            right += 1
            left += 1
        elif s[right] != " " and s[left] == " ":
            left = right
            right += 1
        else:
            right += 1
    #         转最后一个单词
    helper(s, left, right - 1)
    # print(s)
    res = list()
    find_kongge = False
    for item in s:
        if item == ' ':
            if find_kongge is False:
                find_kongge = True
                res.append(item)
            else:
                continue
        elif item != ' ':
            res.append(item)
            find_kongge = False
    # print(res)
    return "".join(res)


res = reverseWords('abc  edfadad')
print(res)