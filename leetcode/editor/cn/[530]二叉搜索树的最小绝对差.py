# 给定一个所有节点为非负值的二叉搜索树，求树中任意两节点的差的绝对值的最小值。
#
# 示例 : 
#
# 
# 输入:
#
#   1
#    \
#     3
#    /
#   2
#
# 输出:
# 1
#
# 解释:
# 最小绝对差为1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
# 
#
# 注意: 树中至少有2个节点。 
# Related Topics 树

# 二叉树的性质，左子树的值小于当前节点，而右子树的值大于当前节点。基于这个思路，可以先中序遍历二叉树，得到的数组即为升序排序，然后遍历一次数组既可以得到差值最小。

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return
        values = []
        values = self.inorder(root, values)
        return min(
            [abs(values[i + 1] - values[i]) for i in range(len(values) - 1)])

    def inorder(self, root, values):
        if root is None:
            return
        self.inorder(root.left, values)
        values.append(root.val)
        self.inorder(root.right, values)
        return values

# leetcode submit region end(Prohibit modification and deletion)
