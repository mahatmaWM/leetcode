# 给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。
# s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。
#
# 示例 1: 
# 给定的树 s:
#
# 
#     3
#    / \
#   4   5
#  / \
# 1   2
# 
#
# 给定的树 t： 
#
# 
#   4 
#  / \
# 1   2
# 
#
# 返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。 
#
# 示例 2: 
# 给定的树 s：
#
# 
#     3
#    / \
#   4   5
#  / \
# 1   2
#    /
#   0
# 
#
# 给定的树 t： 
#
# 
#   4
#  / \
# 1   2
# 
#
# 返回 false。 
# Related Topics 树

# 思路：
# 判断一棵树是否是另一棵的子树，通过前序遍历的结果是否存在包含关系实现


# # 这个函数把树序列化为一个元组
# toTuple = lambda n: (n.val, toTup(n.left), toTup(n.right)) if n else None
# # 把元组转化为字符串以方便比较
# return str(toTuple(t)) in str(toTuple(s))

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        def pre_order(root, res):
            if root:
                res.append(str(root.val))
                pre_order(root.left, res)
                pre_order(root.right, res)
            else:
                res.append('#')

        s_list, t_list = [], []
        pre_order(s, s_list)
        pre_order(t, t_list)
        # 将列表转为字符串进行比较，前端加“，”防止出现“2,#,#”in“12,#,#”中的情况
        return ',' + ','.join(t_list) in ',' + ','.join(s_list)

# leetcode submit region end(Prohibit modification and deletion)
