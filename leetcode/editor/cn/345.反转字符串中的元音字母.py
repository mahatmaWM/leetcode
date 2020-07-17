#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#
# https://leetcode-cn.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (50.07%)
# Likes:    98
# Dislikes: 0
# Total Accepted:    39.4K
# Total Submissions: 78.4K
# Testcase Example:  '"hello"'
#
# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
#
# 示例 1:
#
# 输入: "hello"
# 输出: "holle"
#
#
# 示例 2:
#
# 输入: "leetcode"
# 输出: "leotcede"
#
# 说明:
# 元音字母不包含字母"y"。
#
#


# @lc code=start
class Solution:
    # 注意这种反转的场景，[left, right]两边闭合的区间会少遍历一次
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'O', 'E', 'I', 'U']
        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)


# @lc code=end
