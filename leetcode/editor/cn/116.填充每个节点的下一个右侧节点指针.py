# 给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
#
# struct Node {
#  int val;
#  Node *left;
#  Node *right;
#  Node *next;
# }
#
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。 
#
# 初始状态下，所有 next 指针都被设置为 NULL。 
#
# 
#
# 示例：
# 给定完美二叉树，
#
#      1
#    /  \
#   2    3
#  / \  / \
# 4  5  6  7
# 调用你的函数后，该完美二叉树变为：
#
#      1 -> NULL
#    /  \
#   2 -> 3 -> NULL
#  / \  / \
# 4->5->6->7 -> NULL
#
# 输入：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}
#
# 输出：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":{"$id":"6","left":null,"next":null,"right":null,"val":7},"right":null,"val":6},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"7","left":{"$ref":"5"},"next":null,"right":{"$ref":"6"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"7"},"val":1}
#
# 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。
# 
#
# 
#
# 提示： 
#
# 
# 你只能使用常量级额外空间。 
# 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。 
# 
# Related Topics 树 深度优先搜索

# 思路：
# 借鉴层次遍历的思想，单独获得每一层节点的list然后对每一个list的next进行赋值。
# 空间复杂度O(k),k表示最后一层的叶节点数量，时间复杂度O（n）


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is not None:
            last_level = [root]
            while True:
                current_level = []
                while last_level:
                    temp_node = last_level.pop(0)
                    current_level.append(temp_node.left)
                    current_level.append(temp_node.right)

                # meet leaf, break
                if current_level[0] is None:
                    break

                for i in range(len(current_level) - 1):
                    current_level[i].next = current_level[i + 1]

                last_level = current_level
            return root

# leetcode submit region end(Prohibit modification and deletion)
