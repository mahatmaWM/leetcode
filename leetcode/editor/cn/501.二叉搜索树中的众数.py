#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#
# https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/description/
#
# algorithms
# Easy (44.88%)
# Likes:    115
# Dislikes: 0
# Total Accepted:    15.1K
# Total Submissions: 33.6K
# Testcase Example:  '[1,null,2,2]'
#
# 给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。
#
# 假定 BST 有如下定义：
#
#
# 结点左子树中所含结点的值小于等于当前结点的值
# 结点右子树中所含结点的值大于等于当前结点的值
# 左子树和右子树都是二叉搜索树
#
#
# 例如：
# 给定 BST [1,null,2,2],
#
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  2
#
#
# 返回[2].
#
# 提示：如果众数超过1个，不需考虑输出顺序
#
# 进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution1:
    # 如果不限制空间的话，先中序遍历一下，然后对结果nums进行计数统计
    def findMode(self, root: TreeNode) -> List[int]:
        if not root: return []
        nums = []

        def helper(node):
            nonlocal nums
            if not node: return
            helper(node.left)
            nums.append(node.val)
            helper(node.right)

        helper(root)

        import collections
        cnt = collections.Counter(nums).most_common()
        res = []
        for k, v in cnt:
            if v == cnt[0][1]:
                res.append(k)
            else:
                break
        return res


class Solution:

    def findMode(self, root: TreeNode) -> List[int]:
        pre = None
        ret = []
        ret_count, max_count, cur_count = 0, 0, 0

        def inOrder(root):
            nonlocal pre, ret_count, cur_count, max_count, ret
            if not root: return
            inOrder(root.left)
            if pre and pre.val == root.val:
                cur_count += 1
            else:
                cur_count = 1

            if cur_count > max_count:
                max_count = cur_count
                ret_count = 1
            elif cur_count == max_count:
                if len(ret): ret[ret_count] = root.val
                ret_count += 1

            pre = root
            inOrder(root.right)

        # 第一次遍历，找出max_count的值，知道了众数出现的次数
        inOrder(root)
        pre = None
        ret = [0] * ret_count
        ret_count, cur_count = 0, 0
        # 第二次遍历，把出现次数为max_count的众数放入结果
        inOrder(root)
        return ret


# @lc code=end
