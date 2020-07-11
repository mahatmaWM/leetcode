#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (30.74%)
# Likes:    2315
# Dislikes: 0
# Total Accepted:    293.5K
# Total Submissions: 954.7K
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#
#
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"
#
#
#


# @lc code=start
class Solution:
    # 思路一：从大到小的枚举所有子串，判断子串是否为回文。这种暴力枚举复杂度为n^3。
    # 思路二：动态规划思路，复杂度为N^2：
    # 状态：mem[l][r]为真或假，代表了s[l:r+1]表示的字符串是不是回文串，包含r。
    # 然后使用两个指针暴力枚举的过程中，利用记录的mem信息+动态规划的思想，避免了很多不必要的判断。
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1: return s

        mem = [[False] * n for _ in range(n)]
        lmax = 1
        res = s[0]
        for end in range(1, n):
            for start in range(end):
                # 只有两个字符时 或者 根据之前的回文串继续延伸得到更长回文
                if s[start] == s[end] and (end - start <= 2 or mem[start + 1][end - 1]):
                    mem[start][end] = True
                    cur_len = end - start + 1
                    if cur_len > lmax:
                        lmax = cur_len
                        res = s[start:end + 1]
        return res


# @lc code=end
