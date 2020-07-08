#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找常用字符
#
# https://leetcode-cn.com/problems/find-common-characters/description/
#
# algorithms
# Easy (67.77%)
# Likes:    79
# Dislikes: 0
# Total Accepted:    13.4K
# Total Submissions: 19.7K
# Testcase Example:  '["bella","label","roller"]'
#
# 给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3
# 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。
#
# 你可以按任意顺序返回答案。
#
#
#
# 示例 1：
#
# 输入：["bella","label","roller"]
# 输出：["e","l","l"]
#
#
# 示例 2：
#
# 输入：["cool","lock","cook"]
# 输出：["c","o"]
#
#
#
#
# 提示：
#
#
# 1 <= A.length <= 100
# 1 <= A[i].length <= 100
# A[i][j] 是小写字母
#
#
#


# @lc code=start
class Solution:
    # 取出第一个单词中的所有字母组成集合，然后考察该集合中的字母在每个单词中出现过的最小次数
    def commonChars(self, A: List[str]) -> List[str]:
        res = []
        if not A: return res

        key = set(A[0])
        for k in key:
            minnum = min(a.count(k) for a in A)
            res += minnum * k
        return res


# @lc code=end
