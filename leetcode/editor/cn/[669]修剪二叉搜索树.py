# 给定一个二叉搜索树，同时给定最小边界L 和最大边界 R。
# 通过修剪二叉搜索树，使得所有节点的值在[L, R]中 (R>=L) 。
# 你可能需要改变树的根节点，所以结果应当返回修剪好的二叉搜索树的新的根节点。
#
# 示例 1: 
#
# 
# 输入:
#    1
#   / \
#  0   2
#
#  L = 1
#  R = 2
#
# 输出:
#    1
#      \
#       2
# 
#
# 示例 2: 
#
# 
# 输入:
#    3
#   / \
#  0   4
#   \
#    2
#   /
#  1
#
#  L = 1
#  R = 3
#
# 输出:
#      3
#     / 
#   2   
#  /
# 1
# 
# Related Topics 树

# 题目意思就是给定一棵二叉排序树，以及一个最小值和一个最大值，让你把树中低于最小值和高于最大值的数删了，并返回此时树的根节点。
#
# 这一题用递归做，思路：
# 当 node.val>R 时，继续修剪节点左侧，右子树一定比R大。
# 当 node.val<L 时，继续修剪节点右侧，左子树一定比L小。
# 否则，我们修剪树的两边。


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """

        def trim(node):
            if not node:
                return None
            elif node.val > R:
                return trim(node.left)
            elif node.val < L:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)

# leetcode submit region end(Prohibit modification and deletion)
