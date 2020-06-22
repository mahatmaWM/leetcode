# 给定两个二叉树，编写一个函数来检验它们是否相同。
#
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。 
#
# 示例 1: 
#
# 输入:      1         1
#          / \       / \
#         2   3     2   3
#
#        [1,2,3],   [1,2,3]
#
# 输出: true
#
# 示例 2: 
#
# 输入:     1          1
#          /           \
#         2             2
#
#        [1,2],     [1,null,2]
#
# 输出: false
# 
#
# 示例 3: 
#
# 输入:      1         1
#          / \       / \
#         2   1     1   2
#
#        [1,2,1],   [1,1,2]
#
# 输出: false
# 
# Related Topics 树 深度优先搜索

# 1、返回条件，两个节点都为none，则返回真，否则返回假。
# 2、如果当前两个节点的值相同，则依次对比左孩子和右孩子。

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True

        if (p is None and q is not None) or (p is not None and q is None):
            return False

        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(
                p.right, q.right)
        else:
            return False

# leetcode submit region end(Prohibit modification and deletion)
