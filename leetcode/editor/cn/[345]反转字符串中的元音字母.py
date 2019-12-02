# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
#
# 示例 1: 
#
# 输入: "hello"
# 输出: "holle"
# 
#
# 示例 2: 
#
# 输入: "leetcode"
# 输出: "leotcede"
#
# 说明: 
# 元音字母不包含字母"y"。
# Related Topics 双指针 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        left, right = 0, len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'O', 'E', 'I', 'U']
        while left < right:
            if s[left] not in vowels:
                left += 1
                continue
            if s[right] not in vowels:
                right -= 1
                continue

            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)

# leetcode submit region end(Prohibit modification and deletion)
