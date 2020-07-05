#
# @lc app=leetcode.cn id=307 lang=python3
#
# [307] 区域和检索 - 数组可修改
#
# https://leetcode-cn.com/problems/range-sum-query-mutable/description/
#
# algorithms
# Medium (55.98%)
# Likes:    144
# Dislikes: 0
# Total Accepted:    11.4K
# Total Submissions: 20.3K
# Testcase Example:  '["NumArray","sumRange","update","sumRange"]\n[[[1,3,5]],[0,2],[1,2],[0,2]]'
#
# 给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
#
# update(i, val) 函数可以通过将下标为 i 的数值更新为 val，从而对数列进行修改。
#
# 示例:
#
# Given nums = [1, 3, 5]
#
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
#
#
# 说明:
#
#
# 数组仅可以在 update 函数下进行修改。
# 你可以假设 update 函数与 sumRange 函数的调用次数是均匀分布的。
#
#
#
# @lc code=start
class SegmentNode:

    def __init__(self, start, end):
        # node节点的区间[start, end]，两边都闭
        self.start = start
        self.end = end
        # 区间和
        self.sum = 0
        # 左右子树
        self.left = None
        self.right = None
class NumArray1:
    # 由于数组可以被修改，所以和303题情况不同，这里用 线段树 segment-tree 数据结构来处理
    # 线段树 本质类似完全二叉树，每个节点的区间都被两个子节点平分
    def __init__(self, nums: List[int]):

        def buildTree(l, r):
            if l > r: return None
            if l == r:  # 叶子
                n = SegmentNode(l, r)
                n.sum = nums[l]
                return n
            root = SegmentNode(l, r)
            mid = (l + r) // 2
            root.left, root.right = buildTree(l, mid), buildTree(mid + 1, r)
            root.sum = root.left.sum + root.right.sum
            return root

        self.root = buildTree(0, len(nums) - 1)

    def update(self, i: int, val: int) -> None:

        def updateTree(root, i, val):
            if root.start == root.end:
                root.sum = val
                return val
            # 递归更新树
            mid = (root.start + root.end) // 2
            if i <= mid:
                updateTree(root.left, i, val)
            else:
                updateTree(root.right, i, val)
            root.sum = root.left.sum + root.right.sum
            return root.sum

        updateTree(self.root, i, val)

    def sumRange(self, i: int, j: int) -> int:

        def findNode(root, x, y):
            # 叶子节点
            if root.start == x and root.end == y: return root.sum
            mid = (root.start + root.end) // 2
            if y <= mid: return findNode(root.left, x, y)
            if x > mid: return findNode(root.right, x, y)
            return findNode(root.left, x, mid) + findNode(root.right, mid + 1, y)

        return findNode(self.root, i, j)


class NumArray(object):
    # 由于数组可以被修改，所以和303题情况不同，这里用 树状数组 binary-indexed-tree 数据结构来处理
    def __init__(self, nums):
        self.nums = nums[:]
        self.sum = [0 for i in range(len(nums) + 1)]
        for i in range(len(nums)):
            self.initialize(i, nums[i])

    def initialize(self, i, val):
        i += 1
        while i < len(self.nums) + 1:
            self.sum[i] += val
            # lowbit的操作，保证了logN
            i += (i & -i)

    def update(self, i, val):
        diff = val - self.nums[i]
        self.nums[i] = val
        self.initialize(i, diff)

    def left_sum(self, i):
        i += 1
        total = 0
        while i > 0:
            total += self.sum[i]
            i -= (i & -i)
        return total

    def sumRange(self, i, j):
        return self.left_sum(j) - self.left_sum(i - 1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
# @lc code=end
