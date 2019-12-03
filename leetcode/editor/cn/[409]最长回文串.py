# 给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
#
# 在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。 
#
# 注意: 
# 假设字符串的长度不会超过 1010。
#
# 示例 1: 
#
# 
# 输入:
# "abccccdd"
#
# 输出:
# 7
#
# 解释:
# 我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
# 
# Related Topics 哈希表

# 1、记录s中每个字母出现的次数。
# 2、出现次数为偶数的字母都可以用来构造回文，出现次数为奇数的，可以用其减1的长度来构造回文。
# 3、最后再添加一个出现次数为奇数的字符。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict1 = {}
        j = 0
        z = 0
        for i in range(len(s)):
            if s[i] in dict1:
                dict1[s[i]] += 1
            else:
                dict1[s[i]] = 1
        for v in dict1:
            if (dict1[v] + 1) % 2 == 0:
                j += (dict1[v] - 1)
                z += 1
            if dict1[v] % 2 == 0:
                j += dict1[v]
        if z > 0:
            return j + 1
        else:
            return j

# leetcode submit region end(Prohibit modification and deletion)
