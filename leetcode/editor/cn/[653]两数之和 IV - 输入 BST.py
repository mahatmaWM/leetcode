# 给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。
#
# 案例 1: 
#
# 
# 输入:
#    5
#   / \
#  3   6
# / \   \
# 2   4   7
#
# Target = 9
#
# 输出: True
# 
#
# 
#
# 案例 2: 
#
# 
# 输入:
#    5
#   / \
#  3   6
# / \   \
# 2   4   7
#
# Target = 28
#
# 输出: False
# 
#
# 
# Related Topics 树

# 中序遍历bst，得到升序数组，然后二分查找是否存在目标数对（这里用n2的方法查找）。

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        inorder = lambda node: inorder(node.left) + [node.val] + inorder(node.right) if node else []

        res = inorder(root)
        for i, ele in enumerate(res):
            if k - ele in res and res.index(k - ele) != i:
                return True
        return False

# leetcode submit region end(Prohibit modification and deletion)
