# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
#
# 示例: 
#
# 输入: n = 4, k = 2
# 输出:
# [
#  [2,4],
#  [3,4],
#  [2,3],
#  [1,2],
#  [1,3],
#  [1,4],
# ]
# Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []

        def backtrack(start, k, tmp):
            if k == 0:
                self.res.append(tmp[:])

            # 组合中一个数字只能出现一次，所以从下一位开始选i
            for i in range(start + 1, n + 1):
                tmp.append(i)
                backtrack(i, k - 1, tmp)
                tmp.pop()

        backtrack(0, k, [])
        return self.res

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().combine(n = 4, k = 2))
