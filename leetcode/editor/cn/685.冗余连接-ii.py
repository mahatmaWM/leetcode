#
# @lc app=leetcode.cn id=685 lang=python3
#
# [685] 冗余连接 II
#
# https://leetcode-cn.com/problems/redundant-connection-ii/description/
#
# algorithms
# Hard (34.87%)
# Likes:    71
# Dislikes: 0
# Total Accepted:    3.4K
# Total Submissions: 9.6K
# Testcase Example:  '[[1,2],[1,3],[2,3]]'
#
# 在本问题中，有根树指满足以下条件的有向图。该树只有一个根节点，所有其他节点都是该根节点的后继。每一个节点只有一个父节点，除了根节点没有父节点。
#
# 输入一个有向图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N)
# 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。
#
# 结果图是一个以边组成的二维数组。 每一个边 的元素是一对 [u, v]，用以表示有向图中连接顶点 u 和顶点 v 的边，其中 u 是 v 的一个父节点。
#
# 返回一条能删除的边，使得剩下的图是有N个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。
#
# 示例 1:
#
# 输入: [[1,2], [1,3], [2,3]]
# 输出: [2,3]
# 解释: 给定的有向图如下:
# ⁠ 1
# ⁠/ \
# v   v
# 2-->3
#
#
# 示例 2:
#
# 输入: [[1,2], [2,3], [3,4], [4,1], [1,5]]
# 输出: [4,1]
# 解释: 给定的有向图如下:
# 5 <- 1 -> 2
# ⁠    ^    |
# ⁠    |    v
# ⁠    4 <- 3
#
#
# 注意:
#
#
# 二维数组大小的在3到1000范围内。
# 二维数组中的每个整数在1到N之间，其中 N 是二维数组的大小。
#
#
#


# @lc code=start
class Solution:
    # 1、情况1，多出的边指向某个非root的结点，该结点记为end，它的入度为2，出度不为0，此时答案只可能为指向end的两条边之一，注意这时候答案唯一，删错边可能导致图不联通，无法构成树。
    # 2、情况2，与情况1类似，存在入度为2但出度为0的end结点，此时答案不唯一，删掉指向end的哪条边都能使得图变成树，按照题目要求返回最后环内最后出现的边即可。
    # 3、情况3，多出的边指向root，所有结点的入度都是1，此时答案不唯一，删除环内任意边都可以，按照题目要求返回最后环内最后出现的边即可。
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:

        class UnionFind:

            def __init__(self, n):
                # 记录有多少个连通分量
                self.count = n
                # 记录每个节点的父亲节点
                self.parent = [i for i in range(n)]
                # 新增一个数组记录树的“重量”
                self.rank = [1 for _ in range(n)]

            def get_count(self):
                return self.count

            def find(self, p):
                while p != self.parent[p]:
                    # 进行路径压缩
                    self.parent[p] = self.parent[self.parent[p]]
                    p = self.parent[p]
                return p

            def is_connected(self, p, q):
                return self.find(p) == self.find(q)

            def union(self, p, q):
                p_root = self.find(p)
                q_root = self.find(q)
                if p_root == q_root: return
                # 小树接到大树下面较平衡
                if self.rank[p_root] > self.rank[q_root]:
                    self.parent[q_root] = p_root
                    self.rank[p_root] += self.rank[q_root]
                else:
                    self.parent[p_root] = q_root
                    self.rank[q_root] += self.rank[p_root]
                self.count -= 1

        # 统计所有的节点的入度(1到N)
        in_degree = [0] * (len(edges) + 1)
        end = -1
        for edge in edges:
            in_degree[edge[1]] += 1
            if in_degree[edge[1]] > 1: end = edge[1]

        # 构造一个并查集
        tree = UnionFind(len(edges))

        # 若有end，则为情况1、2，答案为指向end的两条边之一
        if end != -1:
            is_first = True
            edge_first, edge_second = list([]), list([])
            for edge in edges:
                if edge[1] == end:
                    if is_first:
                        is_first = False
                        tree.union(edge[0] - 1, edge[1] - 1)
                        edge_first = edge
                    else:
                        edge_second = edge
                else:
                    tree.union(edge[0] - 1, edge[1] - 1)
            # 看最后是否连通
            return edge_second if tree.get_count() == 1 else edge_first
        else:
            # 否则删除环内最后出现的那条边
            for edge in edges:
                if tree.is_connected(edge[0] - 1, edge[1] - 1): return edge
                tree.union(edge[0] - 1, edge[1] - 1)


# @lc code=end
