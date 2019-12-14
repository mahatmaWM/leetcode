# 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
#
# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）。
# 
#
# 两个字符串完全匹配才算匹配成功。 
#
# 说明: 
#
# 
# s 可能为空，且只包含从 a-z 的小写字母。 
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。 
# 
#
# 示例 1: 
#
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
#
# 示例 2: 
#
# 输入:
# s = "aa"
# p = "*"
# 输出: true
# 解释: '*' 可以匹配任意字符串。
# 
#
# 示例 3: 
#
# 输入:
# s = "cb"
# p = "?a"
# 输出: false
# 解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
# 
#
# 示例 4: 
#
# 输入:
# s = "adceb"
# p = "*a*b"
# 输出: true
# 解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
# 
#
# 示例 5: 
#
# 输入:
# s = "acdcb"
# p = "a*c?b"
# 输入: false
# Related Topics 贪心算法 字符串 动态规划 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
        # 判断s和p的第一位是否匹配成功，条件：s不能为空且p[0]==s[0] or "."
        first = bool(s) and (p[0] == s[0] or p[0] == '?')

        # 看子问题中是否有*号，准备递归
        if len(p) >= 2 and p[1] == '*':
            # 对应（字符+*）出现0次 或者 多次
            return self.isMatch(s, p[2:]) or (first and self.isMatch(s[1:], p))
        else:
            return first and self.isMatch(s[1:], p[1:])

# leetcode submit region end(Prohibit modification and deletion)
