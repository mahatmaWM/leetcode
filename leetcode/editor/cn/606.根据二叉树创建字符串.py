# 你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。
#
# 空节点则用一对空括号 "()" 表示。而且你需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。
#
# 示例 1:
#
#
# 输入: 二叉树: [1,2,3,4]
#       1
#     /   \
#    2     3
#   /
#  4
#
# 输出: "1(2(4))(3)"
#
# 解释: 原本将是“1(2(4)())(3())”，
# 在你省略所有不必要的空括号对之后，
# 它将是“1(2(4))(3)”。
#
#
# 示例 2:
#
#
# 输入: 二叉树: [1,2,3,null,4]
#       1
#     /   \
#    2     3
#     \
#      4
#
# 输出: "1(2()(4))(3)"
#
# 解释: 和第一个示例相似，
# 除了我们不能省略第一个对括号来中断输入和输出之间的一对一映射关系。
#
# Related Topics 树 字符串


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 后序遍历二叉树，注意：如果有右孩子，则必须打印左孩子信息（不管是否为()符号）
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ""

        res = ""
        left = self.tree2str(t.left)
        right = self.tree2str(t.right)

        if left or right:
            res += "(%s)" % left
        if right:
            res += "(%s)" % right
        return str(t.val) + res


# leetcode submit region end(Prohibit modification and deletion)
