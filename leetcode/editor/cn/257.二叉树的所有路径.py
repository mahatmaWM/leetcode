#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#
# https://leetcode-cn.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (64.02%)
# Likes:    271
# Dislikes: 0
# Total Accepted:    40K
# Total Submissions: 62.6K
# Testcase Example:  '[1,2,3,null,5]'
#
# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
#
# 输入:
#
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
#
# 输出: ["1->2->5", "1->3"]
#
# 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
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

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.res = []

        def helper(root, path_list):
            if not root: return
            # 选择
            path_list.append(str(root.val))
            if not root.left and not root.right: self.res.append('->'.join(path_list))
            if root.left: helper(root.left, path_list)
            if root.right: helper(root.right, path_list)
            # 取消选择
            path_list.pop()

        helper(root, [])
        return self.res


# @lc code=end
