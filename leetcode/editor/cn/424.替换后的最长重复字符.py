#
# @lc app=leetcode.cn id=424 lang=python3
#
# [424] 替换后的最长重复字符
#
# https://leetcode-cn.com/problems/longest-repeating-character-replacement/description/
#
# algorithms
# Medium (47.44%)
# Likes:    114
# Dislikes: 0
# Total Accepted:    7.8K
# Total Submissions: 16.4K
# Testcase Example:  '"ABAB"\n2'
#
# 给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k
# 次。在执行上述操作后，找到包含重复字母的最长子串的长度。
#
# 注意:
# 字符串长度 和 k 不会超过 10^4。
#
# 示例 1:
#
# 输入:
# s = "ABAB", k = 2
#
# 输出:
# 4
#
# 解释:
# 用两个'A'替换为两个'B',反之亦然。
#
#
# 示例 2:
#
# 输入:
# s = "AABABBA", k = 1
#
# 输出:
# 4
#
# 解释:
# 将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
# 子串 "BBBB" 有最长重复字母, 答案为 4。
#
# 满足条件 -> 扩张长度1，不满足条件 -> 滑动
# 保存滑动窗口内相同字母出现次数的历史最大值，
# 通过判断窗口宽度(right - left + 1) - maxFreq > K来决定窗口是否做滑动，否则窗口就扩张
# 这里只需要记录历史最大值的原因是我们只需要最终保证输出的是最大长度，无需缩减窗口大小
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        left = 0
        # window存放窗口中某个字符出现的次数
        window = defaultdict(int)
        res = 0
        for right, val in enumerate(s):
            window[val] += 1
            # 找到目前最大字符个数,看该窗口是否多余翻转k个字符
            while right - left + 1 - max(window.values()) > k:
                window[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res

# @lc code=end

