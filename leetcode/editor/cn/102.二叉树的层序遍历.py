#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (62.93%)
# Likes:    531
# Dislikes: 0
# Total Accepted:    145.7K
# Total Submissions: 231.5K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
#
#
#
# 示例：
# 二叉树：[3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
# 返回其层次遍历结果：
#
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    # 广度优先遍历是以层为顺序，将某一层上的所有节点都搜索到了之后才向下一层搜索；
    # 使用队列的性质来进行层次访问。
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root: return []

        import collections
        queue = collections.deque()
        queue.append(root)
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(level)
        return res


class Solution(object):

    def levelOrder(self, root):
        if not root: return []
        self.levels = []

        # 递归的方式实现层次遍历
        def helper(node, level):
            # 递归到新层
            if len(self.levels) == level: self.levels.append([])
            self.levels[level].append(node.val)
            if node.left: helper(node.left, level + 1)
            if node.right: helper(node.right, level + 1)

        helper(root, 0)
        return self.levels
# @lc code=end
