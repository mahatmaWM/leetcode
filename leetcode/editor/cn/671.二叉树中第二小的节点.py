# 给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。如果一个节点有两个子节点的话，那么这个节点的值不大于它的子节点的值。
#
# 给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。 
#
# 示例 1: 
#
# 
# 输入:
#    2
#   / \
#  2   5
#     / \
#    5   7
#
# 输出: 5
# 说明: 最小的值是 2 ，第二小的值是 5 。
# 
#
# 示例 2: 
#
# 
# 输入:
#    2
#   / \
#  2   2
#
# 输出: -1
# 说明: 最小的值是 2, 但是不存在第二小的值。
# 
# Related Topics 树

# 要求一个二叉树的倒数第二个小的值。
# 二叉树的特点是父节点的值会小于子节点的值，父节点要么没有子节点，要不左右孩子节点都有。
#
# 根据定义，根节点的值肯定是二叉树中最小的值，剩下的只需要找到左右子树中比跟节点大的最小值就可以了。
# 对于这个题目，还是考察的二叉树的搜索，第一印象是BFS。
# 这里先序遍历二叉树，对于当前节点，如果大于整颗树的root节点值大，则存起来。

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [float('inf')]

        def traverse(node):
            if not node:
                return
            if root.val < node.val < res[0]:
                res[0] = node.val
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return -1 if res[0] == float('inf') else res[0]

# leetcode submit region end(Prohibit modification and deletion)
