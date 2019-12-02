#给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。 
#
# 
#
# 在杨辉三角中，每个数是它左上方和右上方的数的和。 
#
# 示例: 
#
# 输入: 3
#输出: [1,3,3,1]
# 
#
# 进阶： 
#
# 你可以优化你的算法到 O(k) 空间复杂度吗？ 
# Related Topics 数组



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        l = [1]
        import copy
        for n in range(1, rowIndex + 1):
            e = copy.deepcopy(l)
            for i in range(1, n):
                l[i] = e[i] + e[i - 1]
            l.append(1)
            print(l)
        return l
        
#leetcode submit region end(Prohibit modification and deletion)
