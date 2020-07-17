#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#
# https://leetcode-cn.com/problems/reverse-only-letters/description/
#
# algorithms
# Easy (55.19%)
# Likes:    46
# Dislikes: 0
# Total Accepted:    13.1K
# Total Submissions: 23.7K
# Testcase Example:  '"ab-cd"'
#
# 给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。
#
#
#
#
#
#
# 示例 1：
#
# 输入："ab-cd"
# 输出："dc-ba"
#
#
# 示例 2：
#
# 输入："a-bC-dEf-ghIj"
# 输出："j-Ih-gfE-dCba"
#
#
# 示例 3：
#
# 输入："Test1ng-Leet=code-Q!"
# 输出："Qedo1ct-eeLg=ntse-T!"
#
#
#
#
# 提示：
#
#
# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122
# S 中不包含 \ or "
#
#
#


# @lc code=start
class Solution:
    # 注意这种反转的场景，[left, right]两边闭合的区间会少遍历一次
    def reverseOnlyLetters(self, S: str) -> str:
        slist = list(S)
        left, right = 0, len(slist) - 1
        while left < right:
            while left < right and not S[left].isalpha():
                left += 1
            while left < right and not S[right].isalpha():
                right -= 1
            slist[left], slist[right] = slist[right], slist[left]
            left += 1
            right -= 1
        return "".join(slist)


# @lc code=end
