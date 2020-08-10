#
# @lc app=leetcode.cn id=1483 lang=python3
#
# [1483] 树节点的第 K 个祖先
#
# https://leetcode-cn.com/problems/kth-ancestor-of-a-tree-node/description/
#
# algorithms
# Hard (20.93%)
# Likes:    45
# Dislikes: 0
# Total Accepted:    1.9K
# Total Submissions: 7.3K
# Testcase Example:  '["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]\n' +  '[[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]]'
#
# 给你一棵树，树上有 n 个节点，按从 0 到 n-1 编号。树以父节点数组的形式给出，其中 parent[i] 是节点 i 的父节点。树的根节点是编号为
# 0 的节点。
#
# 请你设计并实现 getKthAncestor(int node, int k) 函数，函数返回节点 node 的第 k
# 个祖先节点。如果不存在这样的祖先节点，返回 -1 。
#
# 树节点的第 k 个祖先节点是从该节点到根节点路径上的第 k 个节点。
#
#
#
# 示例：
#
#
#
# 输入：
# ["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
# [[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]]
#
# 输出：
# [null,1,0,-1]
#
# 解释：
# TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);
#
# treeAncestor.getKthAncestor(3, 1);  // 返回 1 ，它是 3 的父节点
# treeAncestor.getKthAncestor(5, 2);  // 返回 0 ，它是 5 的祖父节点
# treeAncestor.getKthAncestor(6, 3);  // 返回 -1 因为不存在满足要求的祖先节点
#
#
#
#
# 提示：
#
#
# 1 <= k <= n <= 5*10^4
# parent[0] == -1 表示编号为 0 的节点是根节点。
# 对于所有的 0 < i < n ，0 <= parent[i] < n 总成立
# 0 <= node < n
# 至多查询 5*10^4 次
#
#
#

# @lc code=start
class TreeAncestor:
    # def __init__(self, n: int, parent: List[int]):
    #     self.n = n
    #     self.parent = parent
    #     self.maps = {}
    #     for i in range(self.n):
    #         self.maps[i] = parent[i]

    # def getKthAncestor(self, node: int, k: int) -> int:
    #     while k:
    #         if node==-1: return -1
    #         node = self.maps[node]
    #         k-=1
    #     return node

    def __init__(self, n: int, parent: List[int]):
        self.res = [[-1] * 20 for _ in range(n)]  # res[node][i]代表node的第2^i个父节点
        # 边界条件
        for i in range(n):
            self.res[i][0] = parent[i]
        # 动态规划填充res数组
        for node in range(n):
            for k in range(1, 20):
                if self.res[node][k - 1] != -1:
                    self.res[node][k] = self.res[self.res[node][k - 1]][k - 1]
        # print(self.res)

    def getKthAncestor(self, node: int, k: int) -> int:
        # k用二进制表示
        #        0
        #       1
        #      2
        #     3
        #    4
        #   5
        #  6
        # node 6 的 第5个父节点   （5 ： 0101）
        # 等于 node 6 的 第2^0=1个父节点 的 第2^2=4个父节点
        # logk次查找
        ind = 0
        while k:
            ys = k % 2
            if ys == 1:
                node = self.res[node][ind]
                if node == -1: return node
            k = k // 2
            ind += 1
        return node




# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
# @lc code=end
