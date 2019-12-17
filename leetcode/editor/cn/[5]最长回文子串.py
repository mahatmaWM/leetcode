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

# 动态规划思路：
# 状态：mem[l][r]为真或假，代表了s[l:r+1]表示的字符串是不是回文串，包含r。

# 然后在暴力枚举的过程中，利用记录的mem信息+动态规划的思想，避免了很多不必要的判断。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n <= 1:
            return s

        mem = [[False] * n for _ in range(n)]

        longest_l = 1
        res = s[0]

        for right in range(1, n):
            for left in range(right):
                # 两个字符时 或者 由当前回文串可以继续延长回文
                if s[left] == s[right] and \
                        (right - left <= 2 or mem[left + 1][right - 1]):
                    mem[left][right] = True
                    cur_len = right - left + 1
                    if cur_len > longest_l:
                        longest_l = cur_len
                        res = s[left:right + 1]
        return res


# leetcode submit region end(Prohibit modification and deletion)
def main():
    print(Solution().longestPalindrome(s="babad"))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
