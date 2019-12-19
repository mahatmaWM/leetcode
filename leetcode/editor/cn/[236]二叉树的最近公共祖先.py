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

# 整体思路：dfs遍历树，查找是否出现p或者q节点，在dfs的过程中更新祖先节点。

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

        # 返回是否找到了p或者q节点
        def dfs(node):
            # 终止递归，到叶子节点或者已经找到时 return
            if not node:
                return False
            if node == p or node == q:
                self.result = node
                return True
            # 递归的 递 部分
            left_result = dfs(node.left)
            right_result = dfs(node.right)

            # 递归的 归 部分，如果左右同时找到，则更新结果，或者找到一个也return
            if left_result and right_result:
                self.result = node
                return True

            if left_result or right_result:
                return True

        dfs(root)
        return self.result

# leetcode submit region end(Prohibit modification and deletion)
