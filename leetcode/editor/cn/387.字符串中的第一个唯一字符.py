# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
#
# 案例:
#
#
# s = "leetcode"
# 返回 0.
#
# s = "loveleetcode",
# 返回 2.
#
#
#
#
# 注意事项：您可以假定该字符串只包含小写字母。
# Related Topics 哈希表 字符串

# 思路：
# 统计字母次数，然后依次遍历字符串，遇到结果即输出

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        counter = collections.Counter(s)
        for i in range(len(s)):
            if counter[s[i]] == 1: return i
        return -1


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    print(Solution().firstUniqChar(s="loveleetcode"))
