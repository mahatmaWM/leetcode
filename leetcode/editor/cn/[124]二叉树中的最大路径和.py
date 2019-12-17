# 给定一个非空二叉树，返回其最大路径和。
#
# 本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。 
#
# 示例 1: 
#
# 输入: [1,2,3]
#
#       1
#      / \
#     2   3
#
# 输出: 6
# 
#
# 示例 2: 
#
# 输入: [-10,9,20,null,null,15,7]
#
#    -10
#    / \
#   9  20
#     /  \
#    15   7
#
# 输出: 42
# Related Topics 树 深度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_sum = float('-inf')

        # 返回node节点所能贡献的最大路径和
        def dfs(node):
            if not node:
                return 0

            # 注意node节点的左右孩子有可能会贡献一个负值，这时需要置为0
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)
            self.max_sum = max(self.max_sum, node.val + left_gain + right_gain)
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.max_sum


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(Solution().maxPathSum(root=root))
