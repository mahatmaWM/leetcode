# 给定一个字符串和一个字符串字典，找到字典里面最长的字符串，该字符串可以通过删除给定字符串的某些字符来得到。
# 如果答案不止一个，返回长度最长且字典顺序最小的字符串。如果答案不存在，则返回空字符串。
#
# 示例 1: 
#
# 
# 输入:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
#
# 输出:
# "apple"
# 
#
# 示例 2: 
#
# 
# 输入:
# s = "abpcplea", d = ["a","b","c"]
#
# 输出:
# "a"
# 
#
# 说明: 
#
# 
# 所有输入的字符串只包含小写字母。 
# 字典的大小不会超过 1000。 
# 所有输入的字符串长度不会超过 1000。 
# 
# Related Topics 排序 双指针

# 1、首先把字典按照长度和字典序排序
# 2、依次检查排序后的字典中的每个但是是否可以由s得到
# 3、找到就返回结果

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d.sort(key=lambda x: (-len(x), x))

        def isSubseq(word, s):
            i = 0
            for c in s:
                if c == word[i]:
                    i += 1
                if i == len(word):
                    return True
            return False

        for word in d:
            if isSubseq(word, s):
                return word
        return ""

# leetcode submit region end(Prohibit modification and deletion)
