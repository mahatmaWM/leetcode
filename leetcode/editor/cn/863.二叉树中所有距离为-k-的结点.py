#
# @lc app=leetcode.cn id=863 lang=python3
#
# [863] 二叉树中所有距离为 K 的结点
#
# https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree/description/
#
# algorithms
# Medium (49.89%)
# Likes:    126
# Dislikes: 0
# Total Accepted:    5.7K
# Total Submissions: 11.4K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n2'
#
# 给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。
#
# 返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。
#
#
#
#
#
#
# 示例 1：
#
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
# 输出：[7,4,1]
# 解释：
# 所求结点为与目标结点（值为 5）距离为 2 的结点，
# 值分别为 7，4，以及 1
#
#
#
# 注意，输入的 "root" 和 "target" 实际上是树上的结点。
# 上面的输入仅仅是对这些对象进行了序列化描述。
#
#
#
#
# 提示：
#
#
# 给定的树是非空的。
# 树上的每个结点都具有唯一的值 0 <= node.val <= 500 。
# 目标结点 target 是树上的结点。
# 0 <= K <= 1000.
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
    # 本题中涉及到二叉树中距离的求解，那么如何在二叉树中求两个节点的距离？
    # 答案是找到两个节点的最近公共祖先，然后分别计算节点与最近公共祖先的高度差，并相加。
    #
    # 那么为了获取所有节点到目标节点的距离，需要获取目标节点与所有节点的最近公共祖先。
    #
    # 首先考虑目标节点的祖先，目标节点的祖先即从根节点到目标节点这一路径, 路径上每个节点都是目标节点的祖先。
    # 目标节点到其的距离为i，那么其他节点到当前祖先节点的距离（高度）应为K-i，由此便很容易计算出所有满足题意的节点。
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        self.path = []
        self.result = []

        # 寻找root节点到目标target之间的路径，这条路径上的每个点都可以作为target的祖先
        def find_path(root, dire):
            if root:
                # 选择当前点为路径
                self.path.append((root, dire))

                if root == target: return True
                if find_path(root.left, 'l') or find_path(root.right, 'r'): return True

                # 取消当前点为路径
                self.path.pop()
            return False

        def find_root_with_distance(root, dire, dis_to_root, goal, nodes):
            if root:
                if dis_to_root == goal: nodes.append(root.val)
                if dis_to_root < goal:
                    # 关于方向的说明，此前已经求出了到达目标节点的路径与方向，观察题例
                    # 如果target=5， 那么对于祖先节点5（自身）来说，可能的节点存在于自身两个方向；
                    # 对于祖先节点3来说，目标节点在其左子树，那么左子树中可能的点已经由下层的节点计算，自身只需要计算右子树即可
                    if dire == 'l':
                        find_root_with_distance(root.right, 'a', dis_to_root + 1, goal, nodes)
                    elif dire == 'r':
                        find_root_with_distance(root.left, 'a', dis_to_root + 1, goal, nodes)
                    else:
                        find_root_with_distance(root.right, 'a', dis_to_root + 1, goal, nodes)
                        find_root_with_distance(root.left, 'a', dis_to_root + 1, goal, nodes)

        # 寻找所有的祖先节点
        find_path(root, None)
        # 把祖先路径上的每个节点都做尝试
        for i, (root, _) in enumerate(self.path):
            # 方向存储在下一个节点中
            if i + 1 < len(self.path):
                dire = self.path[i + 1][1]
            else:
                # 自身作为祖先的时候
                dire = 'a'

            nodes = []
            dis = len(self.path) - i - 1
            goal_dis = K - dis

            find_root_with_distance(root, dire, 0, goal_dis, nodes)
            self.result.extend(nodes)

        return self.result


# @lc code=end
