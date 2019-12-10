# 二叉搜索树中的两个节点被错误地交换。
#
# 请在不改变其结构的情况下，恢复这棵树。 
#
# 示例 1: 
#
# 输入: [1,3,null,null,2]
#
#    1
#   /
#  3
#   \
#    2
#
# 输出: [3,1,null,null,2]
#
#    3
#   /
#  1
#   \
#    2
# 
#
# 示例 2: 
#
# 输入: [3,1,4,null,null,2]
#
#  3
# / \
# 1   4
#    /
#   2
#
# 输出: [2,1,4,null,null,3]
#
#  2
# / \
# 1   4
#    /
#  3 
#
# 进阶: 
#
# 
# 使用 O(n) 空间复杂度的解法很容易实现。 
# 你能想出一个只使用常数空间的解决方案吗？ 
# 
# Related Topics 树 深度优先搜索

# 对于二次搜索树，如果进行中序遍历会形成一个从小到大的递增序列，可以储存中序遍历的结果，检测到数列中不符合要求的节点（因为是两个节点值交换，第一个错误节点会比下一个节点的值还大，第二个错误节点的值会比上一个节点的值还小，找到这两个节点，将其值交换）

# [1, 2, 3, 4, 5, 6]  ==>  [1, 5, 3, 4, 2, 6]
# 在中序遍历的过程中，用一个指针保存上个节点，那么当前节点值应该小于前一个节点的值。否则就存在乱序。
#
# 第一个乱序的数字是pre，第二个乱序的数字是root，所以用两个指针分别保存。

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.pre, self.first, self.second = None, None, None
        self.in_order(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def in_order(self, node):
        if not node:
            return
        self.in_order(node.left)
        if self.pre and self.pre.val > node.val:
            if not self.first:
                self.first = self.pre
            self.second = node
        self.pre = node
        self.in_order(node.right)

# leetcode submit region end(Prohibit modification and deletion)
