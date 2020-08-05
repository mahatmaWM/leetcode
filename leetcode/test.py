def prefix_eval(prefix_expr):
    stack = []
    for i in reversed(prefix_expr.split()):
        # 数字压栈
        if i not in '+-*/':
            stack.append(i)
        else:
            a = int(stack.pop())
            b = int(stack.pop())
            if i == '/':
                stack.append(b / a)
            elif i == '*':
                stack.append(b * a)
            elif i == '+':
                stack.append(b + a)
            elif i == '-':
                # 这里前缀和后缀的区别
                stack.append(a - b)
    return stack[0]

def suffix_eval(suffix_expr):
    stack = []
    for i in suffix_expr.split():
        # 数字压栈
        if i not in '+-*/':
            stack.append(i)
        else:
            a = int(stack.pop())
            b = int(stack.pop())
            if i == '/':
                stack.append(b / a)
            elif i == '*':
                stack.append(b * a)
            elif i == '+':
                stack.append(b + a)
            elif i == '-':
                # 这里前缀和后缀的区别
                stack.append(b - a)
    return stack[0]

def infix_to_prefix(infix_expr):
    prec = {')': 4, '*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    prefix_expr = []
    stack = []
    # 从右到左扫描
    for item in reversed(infix_expr.split()):
        # 操作数，输出到列表末尾
        if item not in prec.keys():
            prefix_expr.append(item)
        # 右括号，入stack
        elif item == ')':
            stack.append(item)
        # 左括号，一直弹stack输出到列表尾部，直到删除相应的右括号
        elif item == '(':
            while stack[-1] != ')':
                prefix_expr.append(stack.pop())
            stack.pop()
        # 运算符*/+-，将其压入stack。
        # 但首先删除已经在stack中具有更高或相等优先级的任何运算符，并将它们加到输出列表中，直到遇到）括号
        else:
            while stack and stack[-1] != ')' and prec[stack[-1]] > prec[item]:
                prefix_expr.append(stack.pop())
            stack.append(item)
    # 检查stack，仍然在栈上的任何运算符都可以删除并加到输出列表的末尾
    while stack:
        prefix_expr.append(stack.pop())
    # 反转序列
    prefix_expr.reverse()
    return ' '.join(prefix_expr)

def infix_to_suffix(infix_expr):
    prec = {')': 4, '*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    suffix_expr = []
    stack = []
    # 从左到右扫描
    for item in infix_expr.split():
        # 操作数，输出到列表末尾
        if item not in prec.keys():
            suffix_expr.append(item)
        # 右括号，入stack
        elif item == '(':
            stack.append(item)
        # 左括号，一直弹stack输出到列表尾部，直到删除相应的右括号
        elif item == ')':
            while stack[-1] != '(':
                suffix_expr.append(stack.pop())
            stack.pop()
        # 运算符*/+-，将其压入stack。
        # 但首先删除已经在stack中具有更高或相等优先级的任何运算符，并将它们加到输出列表中，直到遇到（括号
        else:
            while stack and stack[-1] != '(' and prec[stack[-1]] > prec[item]:
                suffix_expr.append(stack.pop())
            stack.append(item)
    # 检查stack，仍然在栈上的任何运算符都可以删除并加到输出列表的末尾
    while stack:
        suffix_expr.append(stack.pop())
    return ' '.join(suffix_expr)

infix_str = '1 + ( ( 2 + 3 ) * 4 ) - 5'
prefix_output = infix_to_prefix(infix_str)
print(infix_str)
print(prefix_output)
prefix_result = prefix_eval(prefix_output)
print(prefix_result)

infix_str = '1 + ( ( 2 + 3 ) * 4 ) - 5'
suffix_output = infix_to_suffix(infix_str)
print(infix_str)
print(suffix_output)
suffix_result = suffix_eval(suffix_output)
print(suffix_result)