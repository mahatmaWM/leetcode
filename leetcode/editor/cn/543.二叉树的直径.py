# 给定一棵二叉树，你需要计算它的直径长度。
# 一棵二叉树的直径长度是任意两个结点路径长度中的最大值。
# 这条路径可能穿过根结点。
#
# 示例 : 
# 给定二叉树
#
# 
#          1
#         / \
#        2   3
#       / \     
#      4   5    
# 
#
# 返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。 
#
# 注意：两结点之间的路径长度是以它们之间边的数目表示。 
# Related Topics 树

# 思路：
# 把问题转化为求树的高度，经过一个结点node的最长路径的长度，等与它左子树的深度 + 右子树的深度。(定义root的深度为1)。
# 这样递归求树的深度即可。

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_path_length = 0

        def tree_depth(node):
            if not node:
                return 0

            left_depth, right_depth = 0, 0
            if node.left:
                left_depth = tree_depth(node.left)
            if node.right:
                right_depth = tree_depth(node.right)
            self.max_path_length = max(self.max_path_length,
                                       left_depth + right_depth)
            return max(left_depth, right_depth) + 1

        if not root:
            return 0
        tree_depth(root)
        return self.max_path_length


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(Solution().diameterOfBinaryTree(root=root))
