#
# @lc app=leetcode.cn id=395 lang=python3
#
# [395] 至少有K个重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
#
# algorithms
# Medium (43.05%)
# Likes:    163
# Dislikes: 0
# Total Accepted:    10.4K
# Total Submissions: 24.3K
# Testcase Example:  '"aaabb"\n3'
#
# 找到给定字符串（由小写字符组成）中的最长子串 T ， 要求 T 中的每一字符出现次数都不少于 k 。输出 T 的长度。
#
# 示例 1:
#
#
# 输入:
# s = "aaabb", k = 3
#
# 输出:
# 3
#
# 最长子串为 "aaa" ，其中 'a' 重复了 3 次。
#
#
# 示例 2:
#
#
# 输入:
# s = "ababbc", k = 2
#
# 输出:
# 5
#
# 最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。
#
#
#

# @lc code=start
class Solution:
    # 思路：一种直观的想法，蛮干。
    # 1、如果s的长度小于k，则直接返回0.
    # 2、否则找s中出现次数最小的字母，如果某一个字母出现次数小于k，那么他一定不会出现在最终结果中，用它来切分s，
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k: return 0
        for c in set(s):
            if s.count(c) < k:
                # 满足分割条件，进行分割
                return max(self.longestSubstring(t, k) for t in s.split(c))
        # 如果每个字符出现的次数均不小于k，则返回当前字符串的长度
        return len(s)

# @lc code=end

