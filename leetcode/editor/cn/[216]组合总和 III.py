# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
#
# 说明： 
#
# 
# 所有数字都是正整数。 
# 解集不能包含重复的组合。 
# 
#
# 示例 1: 
#
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
# 
#
# 示例 2: 
#
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
# 
# Related Topics 数组 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.res = []

        def backtrack(start, k, tmp_sum, tmp_res):
            if k == 0 and tmp_sum == 0:
                import copy
                self.res.append(tmp_res[:])

            # 组合中一个数字只能出现一次，所以从下一位开始选i
            for i in range(start + 1, 10):
                tmp_res.append(i)
                backtrack(i, k - 1, tmp_sum - i, tmp_res)
                tmp_res.pop()

        backtrack(0, k, n, [])
        return self.res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().combinationSum3(k=3, n=9))
