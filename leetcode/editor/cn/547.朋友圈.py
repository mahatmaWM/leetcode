#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#
# https://leetcode-cn.com/problems/friend-circles/description/
#
# algorithms
# Medium (57.08%)
# Likes:    255
# Dislikes: 0
# Total Accepted:    47.2K
# Total Submissions: 82.7K
# Testcase Example:  '[[1,1,0],[1,1,0],[0,0,1]]'
#
# 班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C
# 的朋友。所谓的朋友圈，是指所有朋友的集合。
#
# 给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j
# 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。
#
# 示例 1:
#
#
# 输入:
# [[1,1,0],
# ⁠[1,1,0],
# ⁠[0,0,1]]
# 输出: 2
# 说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
# 第2个学生自己在一个朋友圈。所以返回2。
#
#
# 示例 2:
#
#
# 输入:
# [[1,1,0],
# ⁠[1,1,1],
# ⁠[0,1,1]]
# 输出: 1
# 说明：已知学生0和学生1互为朋友，学生1和学生2互为朋友，所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，返回1。
#
#
# 注意：
#
#
# N 在[1,200]的范围内。
# 对于所有学生，有M[i][i] = 1。
# 如果有M[i][j] = 1，则有M[j][i] = 1。
#
#
#


# @lc code=start
class Solution:

    def findCircleNum(self, M: List[List[int]]) -> int:

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

        n = len(M)
        tree = UnionFind(n)
        for i in range(0, n - 1, 1):
            for j in range(i + 1, n, 1):
                if M[i][j] == 1: tree.union(i, j)
        return tree.get_count()


# @lc code=end
