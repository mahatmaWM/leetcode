# 所有 DNA 都由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。
# 在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。
#
# 编写一个函数来查找 DNA 分子中所有出现超过一次的 10 个字母长的序列（子串）。 
#
# 
#
# 示例： 
#
# 输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 输出：["AAAAACCCCC", "CCCCCAAAAA"]
# Related Topics 位运算 哈希表

# 思路，10个字母长度的子串序列，出现次数超过一次的。
# 直接遍历记录即可。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        from collections import defaultdict
        res = defaultdict(int)
        for i in range(0, len(s) - 9):
            res[s[i:i + 10]] += 1
        return [k for k, v in res.items() if v > 1]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().findRepeatedDnaSequences(
        s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
