#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (38.24%)
# Likes:    1094
# Dislikes: 0
# Total Accepted:    288.5K
# Total Submissions: 754.2K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
#
#
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#
#
# 说明:
#
# 所有输入只包含小写字母 a-z 。
#
#


# @lc code=start
class Solution:
    # 思路：依次比较strs中的字符串，找到最长的前缀，直到比较完所有的字符串。
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''

        prefix = strs[0]
        for i in range(1, len(strs)):
            if not prefix: return ''
            # 缩小前缀继续和第i个元素找
            while prefix not in strs[i][:len(prefix)] and len(prefix) > 0:
                prefix = prefix[:len(prefix) - 1]
        return prefix


# @lc code=end
