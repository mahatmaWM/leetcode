# 给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
#
# 说明： 
# 你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。
#
# 示例 1: 
#
# 输入: root = [3,1,4,null,2], k = 1
#   3
#  / \
# 1   4
#  \
#    2
# 输出: 1
#
# 示例 2: 
#
# 输入: root = [5,3,6,2,4,null,null,1], k = 3
#       5
#      / \
#     3   6
#    / \
#   2   4
#  /
# 1
# 输出: 3
#
# 进阶： 
# 如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？
# Related Topics 树 二分查找

# 思路：
# 二叉搜索树的中序遍历为递增数组，
# 如果用非递归的方式遍历二叉搜索树，那么第K次遍历到的数字就为结果。

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
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
            if k == 0:
                return node.val
            node = node.right

# leetcode submit region end(Prohibit modification and deletion)
