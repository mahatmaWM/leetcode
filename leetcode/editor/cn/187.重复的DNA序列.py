#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#
# https://leetcode-cn.com/problems/repeated-dna-sequences/description/
#
# algorithms
# Medium (44.51%)
# Likes:    102
# Dislikes: 0
# Total Accepted:    19K
# Total Submissions: 42.5K
# Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
#
# 所有 DNA 都由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA
# 中的重复序列有时会对研究非常有帮助。
#
# 编写一个函数来查找目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。
#
#
#
# 示例：
#
# 输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 输出：["AAAAACCCCC", "CCCCCAAAAA"]
#
#

# @lc code=start
class Solution:
    # 思路，10个字母长度的子串序列，出现次数超过一次的，直接遍历记录即可。
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = collections.defaultdict(int)
        for i in range(0, len(s) - 9):
            res[s[i:i + 10]] += 1
        return [k for k, v in res.items() if v > 1]
# @lc code=end

