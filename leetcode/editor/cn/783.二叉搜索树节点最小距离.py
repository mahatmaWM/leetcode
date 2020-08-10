#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树节点最小距离
#
# https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/description/
#
# algorithms
# Easy (53.06%)
# Likes:    64
# Dislikes: 0
# Total Accepted:    13.9K
# Total Submissions: 26.1K
# Testcase Example:  '[4,2,6,1,3,null,null]'
#
# 给定一个二叉搜索树的根节点 root，返回树中任意两节点的差的最小值。
#
#
#
# 示例：
#
# 输入: root = [4,2,6,1,3,null,null]
# 输出: 1
# 解释:
# 注意，root是树节点对象(TreeNode object)，而不是数组。
#
# 给定的树 [4,2,6,1,3,null,null] 可表示为下图:
#
# ⁠         4
# ⁠       /   \
# ⁠     2      6
# ⁠    / \
# ⁠   1   3
#
# 最小的差值是 1, 它是节点1和节点2的差值, 也是节点3和节点2的差值。
#
#
#
# 注意：
#
#
# 二叉树的大小范围在 2 到 100。
# 二叉树总是有效的，每个节点的值都是整数，且不重复。
# 本题与 530：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/
# 相同
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

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        res, prev = float("inf"), float("-inf")

        # 二叉搜索树中序遍历是严格有序的，在遍历的过程中记录每次current与previous的差值即可
        def in_order(root):
            nonlocal res, prev
            if not root: return

            in_order(root.left)
            res = min(res, abs(root.val - prev))
            prev = root.val
            in_order(root.right)
            return

        in_order(root)
        return res


class Solution1:
    # 非递归版本
    def minDiffInBST(self, root: TreeNode) -> int:
        res, prev = float("inf"), None

        stack = []
        node = root
        while node or stack:
            # 从node节点一直找左边节点
            while node:
                stack.append(node)
                node = node.left
            # 没有左子树了
            node = stack.pop()
            # 处理pop出来的node节点
            if not prev:
                prev = node.val
            else:
                res = min(res, abs(node.val - prev))
                prev = node.val
            node = node.right
        return res
# @lc code=end

