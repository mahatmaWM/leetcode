# 给定一个二叉树
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
# 进阶： 
#
# 
# 你只能使用常量级额外空间。 
# 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。 
# 
#
# 
#
# 示例： 
#
# 
#
# 输入：root = [1,2,3,4,5,null,7]
# 输出：[1,#,2,3,#,4,5,7,#]
# 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。
#
# 
#
# 提示： 
#
# 
# 树中的节点数小于 6000 
# -100 <= node.val <= 100 
# 
#
# 
#
# 
# 
# Related Topics 树 深度优先搜索

# 层次遍历二叉树，然后把每层的节点连起来。注意左右子树是否为空的判断，以及跳出循环的判断。

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


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
                    if temp_node.left:
                        current_level.append(temp_node.left)
                    if temp_node.right:
                        current_level.append(temp_node.right)

                # meet leaf, break
                if len(current_level) == 0 or current_level[0] is None:
                    break

                for i in range(len(current_level) - 1):
                    current_level[i].next = current_level[i + 1]

                last_level = current_level
            return root


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(7)
    print(Solution().connect(root=root))
