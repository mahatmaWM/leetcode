# 给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。
#
# 注意：两个节点之间的路径长度由它们之间的边数表示。 
#
# 示例 1: 
#
# 输入: 
#
# 
#              5
#             / \
#            4   5
#           / \   \
#          1   1   5
# 
#
# 输出: 
#
# 
# 2
# 
#
# 示例 2: 
#
# 输入: 
#
# 
#              1
#             / \
#            4   5
#           / \   \
#          4   4   5
# 
#
# 输出: 
#
# 
# 2
# 
#
# 注意: 给定的二叉树不超过10000个结点。 树的高度不超过1000。 
# Related Topics 树 递归


# 最长路径只有可能是两种情况：
# 1、节点node往一个分支走到某一个位置的一条路径。
# 2、节点node两边可走，最长路径等于两边之和。

# 定义递归函数dfs(node, val)，返回node节点为根的最长路径 和 val值往下走的最大长度

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node, val):
            # 终止条件
            if not node:
                return 0, 0
            # 递归的 递 部分
            left_max_path, left_max_val = dfs(node.left, node.val)
            right_max_path, right_max_val = dfs(node.right, node.val)

            # 递归的 归 部分
            curr_max_path = max(left_max_path, right_max_path,
                                left_max_val + right_max_val)
            if node.val != val:
                return curr_max_path, 0
            else:
                return curr_max_path, max(left_max_val, right_max_val) + 1

        if root:
            return dfs(root, root.val)[0]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(5)
    print(Solution().longestUnivaluePath(root=root))
