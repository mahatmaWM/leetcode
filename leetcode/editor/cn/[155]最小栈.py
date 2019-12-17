# 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
#
# 
# push(x) -- 将元素 x 推入栈中。 
# pop() -- 删除栈顶的元素。 
# top() -- 获取栈顶元素。 
# getMin() -- 检索栈中的最小元素。 
# 
#
# 示例: 
#
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
# 
# Related Topics 栈 设计

# 思路：
# 1、空间换时间，栈里面每个元素为(item, cur_min)的元组。这种方法需要使用On的额外空间。

# 2、另外存储cur_min元素的栈，最小栈即可，这样可以优化掉一些空间。

# 3、还有一种比较巧的办法是使用一个数字来保存当前栈的最小值，而且栈里面不能保存元素，要保存元素与最小值的差值。见MinStack实现
# https://www.cnblogs.com/byrhuangqiang/p/4682354.html

# leetcode submit region begin(Prohibit modification and deletion)
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.diff_stack = []
        self.min = float('-inf')

    def push(self, x):
        """
        每次push元素之前，求与min的差值，并更新min
        """
        if not self.diff_stack:
            self.diff_stack.append(0)
            self.min = x
        else:
            compare = x - self.min
            self.diff_stack.append(compare)
            self.min = x if compare < 0 else self.min

    def pop(self):
        """
        每次pop元素之前，先取diff栈顶元素，如果小于0，说明之前的最小值更大一些，更新min
        """
        diff_top = self.diff_stack[-1]
        self.min = self.min - diff_top if diff_top < 0 else self.min
        self.diff_stack.pop()

    def top(self):
        """
        根据diff栈与当前的min恢复原始入栈的元素，如果diff栈顶元素大于0，
        """
        if len(self.diff_stack) == 0:
            return None
        else:
            return self.min + self.diff_stack[-1] if self.diff_stack[-1] > 0 \
                else self.min

    def getMin(self):
        if len(self.diff_stack) == 0:
            return None
        else:
            return self.min


class MinStack1(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        curMin = self.getMin()
        if curMin is None or x < curMin:
            curMin = x
        self.q.append((x, curMin))

    def pop(self):
        """
        :rtype: None
        """
        self.q.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.q) == 0:
            return None
        else:
            return self.q[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.q) == 0:
            return None
        else:
            return self.q[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# leetcode submit region end(Prohibit modification and deletion)

def main():
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())  # --> 返回 -3.
    minStack.pop()
    print(minStack.top())  # --> 返回 0.
    print(minStack.getMin())  # --> 返回 -2.


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
