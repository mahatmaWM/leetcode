# 给定一个二叉树，它的每个结点都存放着一个整数值。
#
# 找出路径和等于给定数值的路径总数。 
#
# 路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。 
#
# 二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。 
#
# 示例： 
#
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
#      10
#     /  \
#    5   -3
#   / \    \
#  3   2   11
# / \   \
# 3  -2   1
#
# 返回 3。和等于 8 的路径有:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3.  -3 -> 11
# 
# Related Topics 树

# dfs 是深度遍历从node点出发，和为sum的路径。
# pathSum 则是dfs当前节点root，以及从左右孩子再迭代pathSum。

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, node, sum):
        # count the number of paths starting from the node
        ans = 0
        if not node:
            return ans
        if node.val == sum:
            ans += 1
        ans += self.dfs(node.left, sum - node.val)
        ans += self.dfs(node.right, sum - node.val)
        return ans

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        return self.dfs(root, sum) + self.pathSum(root.left,
                                                  sum) + self.pathSum(
            root.right, sum)

# leetcode submit region end(Prohibit modification and deletion)
