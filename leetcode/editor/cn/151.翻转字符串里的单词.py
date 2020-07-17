#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#
# https://leetcode-cn.com/problems/reverse-words-in-a-string/description/
#
# algorithms
# Medium (42.39%)
# Likes:    181
# Dislikes: 0
# Total Accepted:    73.6K
# Total Submissions: 173.6K
# Testcase Example:  '"the sky is blue"'
#
# 给定一个字符串，逐个翻转字符串中的每个单词。
#
#
#
# 示例 1：
#
# 输入: "the sky is blue"
# 输出: "blue is sky the"
#
#
# 示例 2：
#
# 输入: "  hello world!  "
# 输出: "world! hello"
# 解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
#
#
# 示例 3：
#
# 输入: "a good   example"
# 输出: "example good a"
# 解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
#
#
#
#
# 说明：
#
#
# 无空格字符构成一个单词。
# 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
# 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
#
#
#
#
# 进阶：
#
# 请选用 C 语言的用户尝试使用 O(1) 额外空间复杂度的原地解法。
#
#


# @lc code=start
class Solution:
    # 思路，python的字符串不能原位更改，所以无法O1空间。" ".join(s.split()[::-1])一句即可。

    # 模拟整个过程，先翻转整个数组，再翻转单个单词，最后清除头尾多余的空格
    def reverseWords(self, s: str) -> str:
        s = list(s.strip())
        n = len(s)

        # 翻转list s[i,j]
        def reverse(s, i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        # 翻转每个单词，用双指针找到一个单词
        def word_reverse(s):
            w_begin, w_end = 0, 0
            nonlocal n
            while w_begin < n:
                # 找到一个单词首字母
                while w_begin < n and s[w_begin] == " ":
                    w_begin += 1
                w_end = w_begin
                # 找到一个单词末位置
                while w_end < n and s[w_end] != " ":
                    w_end += 1
                reverse(s, w_begin, w_end - 1)
                w_begin = w_end

        def clean_more_space(s):
            left, right = 0, 0
            nonlocal n
            while right < n:
                if s[right] != ' ' or (s[right] == ' ' and s[right + 1] != ' ' and right + 1 < n):
                    s[left] = s[right]
                    left += 1
                    right +=1
                elif s[right] == ' ' and s[right + 1] == ' ' and right + 1 < n:
                    right += 1
            return ''.join(s[0:left])

        reverse(s, 0, n - 1)
        word_reverse(s)
        return clean_more_space(s)


# @lc code=end
