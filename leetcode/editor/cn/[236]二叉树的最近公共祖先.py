# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。” 
#
# 例如，给定如下二叉树: root = [3,5,1,6,2,0,8,null,null,7,4] 
#
# 
#
# 
#
# 示例 1: 
#
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
# 
#
# 示例 2: 
#
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
# 
#
# 
#
# 说明: 
#
# 
# 所有节点的值都是唯一的。 
# p、q 为不同节点且均存在于给定的二叉树中。 
# 
# Related Topics 树

# 整体思路：采用递归，逐层查找。

# step1:设置递归结束条件
# 如果，查找的子树为空时，即node == None，需要结束递归，没有找到，并返回False；
# 如果，p为当前树的子节点，即node == p，那么p、q的最近邻共同祖先就是p本身，记录祖先，返回True；
# 如果，q为当前树的子节点，即node == q，那么p、q的最近邻共同祖先就是q本身，记录祖先，返回True；
# 综上所述：递归结束条件为：root == None or root == p or root == q，返回
#
# step2:查找子树
# 分别在左右子树中找p q，如果左右都返回true，说明当前节点时祖先，如果只有一个为true，说明p q都在一个子树当中，也可以返回true。


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.result = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def dfs(node):
            if not node: return False
            if node == p or node == q:
                self.result = node
                return True

            left_result = dfs(node.left)
            right_result = dfs(node.right)

            # 左右分支都为True
            if left_result and right_result:
                self.result = node
                return True

            if left_result or right_result:
                return True

        dfs(root)
        return self.result

# leetcode submit region end(Prohibit modification and deletion)
