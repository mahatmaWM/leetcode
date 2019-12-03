# 给定一个仅包含小写字母的字符串，去除字符串中重复的字母，使得每个字母只出现一次。需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
#
# 示例 1: 
#
# 输入: "bcabc"
# 输出: "abc"
# 
#
# 示例 2: 
#
# 输入: "cbacdcbc"
# 输出: "acdb"
# Related Topics 栈 贪心算法

# 这个题的难点在于使得结果是字符串顺序最小。
#
# 1、每个字符都必须要出现一次，那么当这个字符只有一次机会的时候，必须添加到结果字符串结尾中去，反之，如果这个字符的次数没有降为0，即后面还有机会，那么可以先把优先级高的放进来，把这个字符放到后面再处理。
#   可以使用一个栈，有点类似单调递增栈的意思，但其实并不是单调栈。思路就是把还可以放到后面的字符弹出栈，留着以后处理，字符序小的插入到对应的位置。
# 2、为了知道每个字符出现了多少次，必须做一次次数统计。
# 3、需要借助一个栈来实现字符串构造的操作。具体操作如下：从输入字符串中逐个读取字符c，并把c的字符统计减一。
#       如果当前字符c已经在栈里面出现，那么跳过。
#       如果当前字符c不在栈里面，那么：
#           如果当前字符c小于栈顶，并且栈顶元素有剩余（后面还能再添加进来），栈不为空，则出栈栈顶，标记栈顶不在栈中。重复该操作直到栈顶元素不满足条件或者栈为空。
#           入栈字符c，并且标记c已经在栈中。


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        import collections
        count = collections.Counter(s)
        stack = []
        visited = collections.defaultdict(bool)
        for c in s:
            count[c] -= 1
            if visited[c]:
                continue
            while stack and count[stack[-1]] and stack[-1] > c:
                visited[stack[-1]] = False
                stack.pop()
            visited[c] = True
            stack.append(c)
        return "".join(stack)

# leetcode submit region end(Prohibit modification and deletion)
