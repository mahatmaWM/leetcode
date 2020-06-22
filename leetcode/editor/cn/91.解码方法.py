# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
#
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。 
#
# 示例 1: 
#
# 输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
# 
#
# 示例 2: 
#
# 输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
# 
# Related Topics 字符串 动态规划


# 动态规划，算法设计如下：
# 首先注意这几种情况，是无法解码的：
# 以0开头，如："0123","000"
# 0前的数字大于2，如："215021"。0前数字小于等于2时，是可以解码的，如："20105"。


# 1、特判，若s为空或者s[0]=="0"，返回0。
# 2、初始化n+1的dp=[0,...,0]，dp[0]=1 dp[1]=1，dp[1]=1表示第一位的解码方法，dp[0]的作用，在于两位时，如："12"，dp[2]=dp[1]+dp[0]。
# 3、遍历s区间[1,n)：
#   3.1、若s[i]=="0"：
#       如果s[i-1]=="1" or s[i-1]=="2"：此时，到当前位置的解码方法dp[i+1]和上上一位的相同，因为上一位和本位置结合在了一起。dp[i+1]=dp[i-1]。
#       否则，返回00，表示无法解码
#   3.2、若s[i]!="0"：
#       则需要判断何时既可以自身解码也可以和前一位结合：
#           （若上一位s[i-1]=="1"，则当前位既可以单独解码 也可以 和上一位结合解码。若上一位s[i-1]=="2"，且"1"<=s[i]<="6"，则当前位既可以单独解码 也可以 和上一位结合解码）
#           综上，s[i-1]=="1" or (s[i-1]=="2" and "1"<=s[i]<="6") 。此时，dp[i+1]=dp[i]+dp[i-1]，等于上一位和上上位的解码方法之和。
#       否则，dp[i+1]=dp[i]
# 4、返回dp[n]


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if not s or s[0] == "0":
            return 0
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(1, n):
            if s[i] == "0":
                if s[i - 1] == "1" or s[i - 1] == "2":
                    dp[i + 1] = dp[i - 1]
                else:
                    return 0
            else:
                if (s[i - 1] == "1" or
                        (s[i - 1] == "2" and "1" <= s[i] <= "6")):
                    dp[i + 1] = dp[i] + dp[i - 1]
                else:
                    dp[i + 1] = dp[i]
        return dp[-1]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().numDecodings(s="226"))
