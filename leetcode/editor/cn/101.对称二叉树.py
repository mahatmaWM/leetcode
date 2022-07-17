#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (52.20%)
# Likes:    855
# Dislikes: 0
# Total Accepted:    161.4K
# Total Submissions: 309.3K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
#
#
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
#
#
#
#
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
#
#
#
#
# 进阶：
#
# 你可以运用递归和迭代两种方法解决这个问题吗？
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # 类似100题
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        # 检查检查p，q两个节点对应的子树是否是否对称
        def check(p, q):
            if not p and not q:
                return True
            elif (not p and q) or (p and not q):
                return False
            else:
                return p.val == q.val and check(p.left, q.right) and check(p.right, q.left)

        return check(root.left, root.right)


# @lc code=end
