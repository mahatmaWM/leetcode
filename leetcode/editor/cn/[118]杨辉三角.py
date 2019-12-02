# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
#
# 
#
# 在杨辉三角中，每个数是它左上方和右上方的数的和。 
#
# 示例: 
#
# 输入: 5
# 输出:
# [
#     [1],
#    [1,1],
#   [1,2,1],
#  [1,3,3,1],
# [1,4,6,4,1]
# ]
# Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(numRows):
            temp = [1] * (i + 1)
            res.append(temp)
            for j in range(1, i):
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
        return res

# leetcode submit region end(Prohibit modification and deletion)
