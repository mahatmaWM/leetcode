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


# 题目很好理解，注意path的长度是边的个数，path可以不经过root。不经过root怎么写？？？
# 和543. Diameter of Binary Tree（python+cpp）类似，这道题目就是求不一定经过root的最长的path的长度。
#
# 只要当前结点的值和它孩子结点的值不一样，就把孩子结点的深度置0。
# 但是注意一定要先遍历再判断，如果先判断再决定要不要遍历的话，那么只要孩子结点的值和父节点不一样，整个子树就都没有遍历，子树里面可能的答案也就没有上传了。


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
        self.max_path = 0

        def tree_depth(node):
            left_depth, right_depth = 0, 0
            if node.left:
                left_depth = tree_depth(node.left)
                if node.left.val != node.val:
                    left_depth = 0
            if node.right:
                right_depth = tree_depth(node.right)
                if node.right.val != node.val:
                    right_depth = 0
            self.max_path = max(self.max_path, left_depth + right_depth)
            return max(left_depth, right_depth) + 1

        if root:
            tree_depth(root)
        return self.max_path

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(5)
    print(Solution().longestUnivaluePath(root=root))
