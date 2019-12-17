# 给定二叉搜索树的根结点 root，返回 L 和 R（含）之间的所有结点的值的和。
#
# 二叉搜索树保证具有唯一的值。 
#
# 
#
# 示例 1： 
#
# 输入：root = [10,5,15,3,7,null,18], L = 7, R = 15
# 输出：32
# 
#
# 示例 2： 
#
# 输入：root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
# 输出：23
# 
#
# 
#
# 提示： 
#
# 
# 树中的结点数量最多为 10000 个。 
# 最终的答案保证小于 2^31。 
# 
# Related Topics 树 递归

# 思路：
# 前序遍历树，根据节点的值来决定是否继续左、右子树的遍历。

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.res = 0

        def pre_order(node):
            if not node:
                return None
            elif node.val > R:
                pre_order(node.left)
            elif node.val < L:
                pre_order(node.right)
            else:
                self.res += node.val
                pre_order(node.left)
                pre_order(node.right)

        pre_order(root)
        return self.res

# leetcode submit region end(Prohibit modification and deletion)
