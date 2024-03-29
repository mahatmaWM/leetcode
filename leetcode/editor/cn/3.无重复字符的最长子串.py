#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (34.74%)
# Likes:    3796
# Dislikes: 0
# Total Accepted:    523.9K
# Total Submissions: 1.5M
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
#
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#
#
# 示例 3:
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
#
#

# @lc code=start
class Solution:
    # 思路：使用left right双指针
    # 窗口使用set可以快速查找，当right插入滑动窗口时，不断检查window的合法性。
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0

        window = set()
        max_len, cur_len = 0, 0
        left, right = 0, 0
        while right < len(s):
            # 检查window的合法性
            while s[right] in window:
                window.remove(s[left])
                left += 1
                cur_len -= 1

            window.add(s[right])
            right += 1
            cur_len += 1
            max_len = max(max_len, cur_len)
        return max_len
# @lc code=end
