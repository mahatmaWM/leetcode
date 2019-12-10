# 给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。
#
# 例如： 
#
# 
# 输入: 二叉搜索树:
#              5
#            /   \
#           2     13
#
# 输出: 转换为累加树:
#             18
#            /   \
#          20     13
# 
# Related Topics 树

# 思路：
# 由于二叉搜索树的左右子树、根的特性，对于节点node，需要求大于它的节点值之和，所以可以 右中左 的遍历方式，用一个变量记录累加和。


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0

        def inorder(node):
            if not node:
                return
            inorder(node.right)
            self.sum += node.val
            node.val = self.sum
            inorder(node.left)

        inorder(root)
        return root

# leetcode submit region end(Prohibit modification and deletion)
