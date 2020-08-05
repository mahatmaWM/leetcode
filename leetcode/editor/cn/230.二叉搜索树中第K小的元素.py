#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#
# https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/description/
#
# algorithms
# Medium (70.61%)
# Likes:    224
# Dislikes: 0
# Total Accepted:    54.9K
# Total Submissions: 77.7K
# Testcase Example:  '[3,1,4,null,2]\n1'
#
# 给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
#
# 说明：
# 你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。
#
# 示例 1:
#
# 输入: root = [3,1,4,null,2], k = 1
# ⁠  3
# ⁠ / \
# ⁠1   4
# ⁠ \
# 2
# 输出: 1
#
# 示例 2:
#
# 输入: root = [5,3,6,2,4,null,null,1], k = 3
# ⁠      5
# ⁠     / \
# ⁠    3   6
# ⁠   / \
# ⁠  2   4
# ⁠ /
# ⁠1
# 输出: 3
#
# 进阶：
# 如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def __init__(self) -> None:
        self.index = 0

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # 中序递归，注意区分left right正常返回 与 None返回的区别？
        def helper(node):
            if not node: return None
            left_return = helper(node.left)
            if left_return is not None: return left_return
            self.index += 1
            if self.index == k: return node.val
            right_return = helper(node.right)
            if right_return is not None: return right_return

        return helper(root)


class Solution1:
    # 如果用非递归的中序方式遍历二叉搜索树，那么第 K 次遍历到的数字就为结果。
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        node = root
        while node or stack:
            # 从根节点开始，一直找左子树
            while node:
                stack.append(node)
                node = node.left
            # while结束表示当前节点node为空，即前一个节点没有左子树了
            node = stack.pop()
            k -= 1
            if k == 0: return node.val
            node = node.right


# @lc code=end
