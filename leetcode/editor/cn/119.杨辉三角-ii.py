#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#
# https://leetcode-cn.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (61.19%)
# Likes:    162
# Dislikes: 0
# Total Accepted:    59.5K
# Total Submissions: 96.8K
# Testcase Example:  '3'
#
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
#
#
#
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 3
# 输出: [1,3,3,1]
#
#
# 进阶：
#
# 你可以优化你的算法到 O(k) 空间复杂度吗？
#
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        l = [1]
        for n in range(1, rowIndex + 1):
            e = copy.deepcopy(l)
            for i in range(1, n):
                l[i] = e[i] + e[i - 1]
            l.append(1)
            # print(l)
        return l
# @lc code=end

