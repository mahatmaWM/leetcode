#
# @lc app=leetcode.cn id=894 lang=python3
#
# [894] 所有可能的满二叉树
#
# https://leetcode-cn.com/problems/all-possible-full-binary-trees/description/
#
# algorithms
# Medium (74.82%)
# Likes:    123
# Dislikes: 0
# Total Accepted:    6.9K
# Total Submissions: 9.1K
# Testcase Example:  '7'
#
# 满二叉树是一类二叉树，其中每个结点恰好有 0 或 2 个子结点。
#
# 返回包含 N 个结点的所有可能满二叉树的列表。 答案的每个元素都是一个可能树的根结点。
#
# 答案中每个树的每个结点都必须有 node.val=0。
#
# 你可以按任何顺序返回树的最终列表。
#
#
#
# 示例：
#
# 输入：7
#
# 输出：[[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
# 解释：
#
#
#
#
#
# 提示：
#
#
# 1 <= N <= 20
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 首先理清两个概念，满二叉树 和 完全二叉树。
    # 满二叉树：要求所有的结点都有0个或者2个叶子结点。
    # 完全二叉树：若设二叉树的深度为h，除第 h 层外，其它各层 (1～h-1) 的结点数都达到最大个数，第 h 层所有的结点都连续集中在最左边。
    # 　(1)所有的叶结点都出现在第k层或k-l层（层次最大的两层）
    # 　(2)对任一结点，如果其右子树的最大层次为L，则其左子树的最大层次为L或L+l。
    # 也就是完全二叉树比满二叉树的形式更加集中。
    #
    # 思路：需要注意的是，如果N是偶数，则一定不能构成满二叉树。
    # 本题用递归的思想，比如对：左边节点 节点i 右边节点，左右都递归构成满二叉树，再和节点i组合在一起即可。
    # 这里用了递归的时候加速，可以把中间状态记录下来。
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N <= 0 or N % 2 == 0: return []

        result = []
        
        self._dict = {1: [TreeNode(0)]}
        if N in self._dict: return self._dict[N]
        for dummy_root in range(1, N, 2):
            for left in self.allPossibleFBT(dummy_root):
                for right in self.allPossibleFBT(N - 1 - dummy_root):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    result += [root]
        self._dict[N] = result
        return result

# @lc code=end

