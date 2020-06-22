# 给定一个二叉树，原地将它展开为链表。
#
# 例如，给定二叉树 
#
#    1
#   / \
#  2   5
# / \   \
# 3   4   6
#
# 将其展开为： 
#
# 1
# \
#  2
#   \
#    3
#     \
#      4
#       \
#        5
#         \
#          6 
# Related Topics 树 深度优先搜索

# 解题思路:
# 递归操作
# 1、把左子树转换成链表, 返回头结点l
# 2、把右子树转换成链表, 返回头结点r
# 3、把l接到root的右子树.左子树置为None
# 4、从root开始遍历到链表尾部,把r接到链表尾部
# 5、返回root节点


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        l = self.flatten(root.left)
        r = self.flatten(root.right)

        root.left = None
        root.right = l

        tmp = root
        while tmp.right:
            tmp = tmp.right
        tmp.right = r

        return root

# leetcode submit region end(Prohibit modification and deletion)
