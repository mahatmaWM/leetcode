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

        for end in range(1, n):
            for start in range(end):
                # 两个字符时 或者 根据当前的回文串继续延伸得到更长回文
                if s[start] == s[end] and \
                        (end - start <= 2 or mem[start + 1][end - 1]):
                    mem[start][end] = True
                    cur_len = end - start + 1
                    if cur_len > longest_l:
                        longest_l = cur_len
                        res = s[start:end + 1]
        return res


# leetcode submit region end(Prohibit modification and deletion)
def main():
    print(Solution().longestPalindrome(s="babad"))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
