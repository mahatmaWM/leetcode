#
# @lc app=leetcode.cn id=386 lang=python3
#
# [386] 字典序排数
#
# https://leetcode-cn.com/problems/lexicographical-numbers/description/
#
# algorithms
# Medium (70.31%)
# Likes:    96
# Dislikes: 0
# Total Accepted:    9.2K
# Total Submissions: 13.1K
# Testcase Example:  '13'
#
# 给定一个整数 n, 返回从 1 到 n 的字典顺序。
#
# 例如，
#
# 给定 n =1 3，返回 [1,10,11,12,13,2,3,4,5,6,7,8,9] 。
#
# 请尽可能的优化算法的时间复杂度和空间复杂度。 输入的数据 n 小于等于 5,000,000。
#
# [int(y) for y in sorted([str(x) for x in (range(1, n+1))])]


# @lc code=start
class Solution:

    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        def dfs(cur):  # cur为根结点
            if cur > n: return
            res.append(cur)
            for i in range(10):
                # 比如叶子结点为14，而n是13，dfs就结束了
                if 10 * cur + i > n: return
                dfs(10 * cur + i)

        # 对1~9的每棵树进行dfs
        for i in range(1, 10):
            dfs(i)
        return res


# @lc code=end
