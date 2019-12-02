# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
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
# Related Topics 字符串 动态规划

# 当遍历到位置i时，
# 1、检查位置i和目前回文的开始字符再往前移动一个，是否组成一个新的回文，新回文长度增加2。
# 2、检查位置i加入到目前回文后，是否组成一个新的回文，新回文长度增加1。
# 如果满足1，可以不用再看2了。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        maxl, start = 0, 0
        for i in range(n):
            if i - maxl >= 1 and \
                    s[i - maxl - 1:i + 1] == s[i - maxl - 1:i + 1][::-1]:
                start = i - maxl - 1
                maxl += 2
                continue
            if i - maxl >= 0 and s[i - maxl:i + 1] == s[i - maxl:i + 1][::-1]:
                start = i - maxl
                maxl += 1
        return s[start:start + maxl]

# leetcode submit region end(Prohibit modification and deletion)
