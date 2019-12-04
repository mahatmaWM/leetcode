# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
#
# 示例 1: 
#
# 
# 输入: "aba"
# 输出: True
# 
#
# 示例 2: 
#
# 
# 输入: "abca"
# 输出: True
# 解释: 你可以删除c字符。
# 
#
# 注意: 
#
# 
# 字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。 
# 
# Related Topics 字符串

# 思路：
# 回文字符串，使用两个指针，前后各一个。
# 当遇到前后字符不一致的时候，有两种情况，删除前面字符或者删除后面字符。
# 由于删除一个字符后剩下的仍旧是字符串，可以直接递归处理了。
# 然后用一个flag，当达到2时，就可以递归结束了。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isPalindrome(self, s, left, right, flag):
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if flag == 1:
                    return False
                flag = 1
                return self.isPalindrome(s, left + 1, right, flag) or \
                       self.isPalindrome(s, left, right - 1, flag)
        return True

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self.isPalindrome(s, 0, len(s) - 1, 0)

# leetcode submit region end(Prohibit modification and deletion)
