# 给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
#
# 例如，从根到叶子节点路径 1->2->3 代表数字 123。 
#
# 计算从根到叶子节点生成的所有数字之和。 
#
# 说明: 叶子节点是指没有子节点的节点。 
#
# 示例 1: 
#
# 输入: [1,2,3]
#    1
#   / \
#  2   3
# 输出: 25
# 解释:
# 从根到叶子节点路径 1->2 代表数字 12.
# 从根到叶子节点路径 1->3 代表数字 13.
# 因此，数字总和 = 12 + 13 = 25.
#
# 示例 2: 
#
# 输入: [4,9,0,5,1]
#    4
#   / \
#  9   0
#  / \
# 5   1
# 输出: 1026
# 解释:
# 从根到叶子节点路径 4->9->5 代表数字 495.
# 从根到叶子节点路径 4->9->1 代表数字 491.
# 从根到叶子节点路径 4->0 代表数字 40.
# 因此，数字总和 = 495 + 491 + 40 = 1026.
# Related Topics 树 深度优先搜索

# 思路，深度优先搜索树，当访问到某一个节点时，需要把当前得到的数字传递给左右子节点。

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def curr_num(node, pre_num):
            if node is None:
                return
            pre_num = pre_num * 10 + node.val
            if node.left is None and node.right is None:
                self.res += pre_num
                return
            curr_num(node.left, pre_num)
            curr_num(node.right, pre_num)

        curr_num(root, 0)

        return self.res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(Solution().sumNumbers(root=root))
