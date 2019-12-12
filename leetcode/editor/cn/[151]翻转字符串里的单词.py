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
# 请选用 C 语言的用户尝试使用 O(1) 额外空间复杂度的原地解法。 
# Related Topics 字符串

# 思路，python的字符串不能原位更改，所以无法O1空间。" ".join(s.split()[::-1])一句即可。

# 或者
# 1、先翻转整个数组
# 2、再翻转单个单词
# 3、清除多余空格

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        n = len(s)

        # 翻转数组
        def reverse(s, i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        # 翻转每个单词，用双指针找到一个单词
        def word_reverse(s):

            left, right = 0, 0
            while left < n:
                # 找到一个单词首字母
                while left < n and s[left] == " ":
                    left += 1
                right = left
                # 找到一个单词末位置
                while right < n and s[right] != " ":
                    right += 1
                reverse(s, left, right - 1)
                left = right

        # 清除多余空格
        def clean_space(s):
            i = 0
            j = 0
            while j < n:
                # 找到一个单词
                while j < n and s[j] == " ":
                    j += 1
                # 单词朝前移
                while j < n and s[j] != " ":
                    s[i] = s[j]
                    i += 1
                    j += 1
                # 移动下一个单词
                while j < n and s[j] == " ":
                    j += 1
                if j < n:
                    s[i] = " "
                    i += 1
            return "".join(s[:i])

        reverse(s, 0, n - 1)
        word_reverse(s)
        return clean_space(s)

# leetcode submit region end(Prohibit modification and deletion)
