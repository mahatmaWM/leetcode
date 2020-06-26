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

# 思路：
# 使用left right 指针模拟滑动窗口，窗口使用set可以快速查找。
# 当right 插入滑动窗口时，不断检查window的合法性。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        window = set()
        max_len, cur_len = 0, 0
        left = 0
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1
                cur_len -= 1

            cur_len += 1
            max_len = max(max_len, cur_len)
            window.add(s[right])
        return max_len


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring(s="abcabcbb"))
