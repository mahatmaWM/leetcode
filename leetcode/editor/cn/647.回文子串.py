# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
#
# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
#
# 示例 1:
#
#
# 输入: "abc"
# 输出: 3
# 解释: 三个回文子串: "a", "b", "c".
#
#
# 示例 2:
#
#
# 输入: "aaa"
# 输出: 6
# 说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
#
#
# 注意:
#
#
# 输入的字符串长度不会超过1000。
#
# Related Topics 字符串 动态规划
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 思路见5题，加上一个计数即可。
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n <= 1: return 1

        res = 0
        mem = [[False] * n for _ in range(n)]
        for end in range(n):
            for start in range(end + 1):
                if s[start] == s[end] and (end - start <= 1 or mem[start + 1][end - 1]):
                    mem[start][end] = True
                    res += 1
        return res


# leetcode submit region end(Prohibit modification and deletion)

