# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。 
#
# 示例 1: 
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 
#
# 示例 2: 
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 
#
# 说明: 
#
# 所有输入只包含小写字母 a-z 。 
# Related Topics 字符串

# 思路：
# 依次比较strs中的字符串，找到最长的前缀，直到比较完所有的字符串。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        prefix = strs[0]
        for i in range(1, len(strs)):
            if not prefix:
                return ''
            else:
                # 缩小前缀继续和第i个元素找
                while prefix not in strs[i][:len(prefix)] and len(prefix) > 0:
                    prefix = prefix[:len(prefix) - 1]
        return prefix

# leetcode submit region end(Prohibit modification and deletion)
