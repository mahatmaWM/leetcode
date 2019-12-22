# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。 
#
# 示例 1: 
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 
#
# 示例 2: 
#
# 输入: "race a car"
# 输出: false
# 
# Related Topics 双指针 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        while left < right:
            while not s[left].isalnum() or not s[left].isalpha():
                left += 1
                # 防止一个字母都没有的情况
                if left == len(s):
                    return False
            while not s[right].isalnum() or not s[right].isalpha():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True


# leetcode submit region end(Prohibit modification and deletion)
def main():
    print(Solution().isPalindrome(s=".,"))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
