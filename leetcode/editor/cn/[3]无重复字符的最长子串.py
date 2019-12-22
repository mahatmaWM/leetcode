# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1: 
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
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 
# Related Topics 哈希表 双指针 字符串 Sliding Window

# 思路：使用滑动窗口

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s):
        window = []
        max_len = 0
        for item in s:
            if item not in window:
                window.append(item)
            else:
                # 发现重复元素，缩小窗口大小
                i = window.index(item)
                window = window[i + 1:]
                window.append(item)
            max_len = max(max_len, len(window))
        return max_len

# leetcode submit region end(Prohibit modification and deletion)
