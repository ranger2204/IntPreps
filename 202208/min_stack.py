from re import X


class MinStack:

    def __init__(self):
        self.main_stack = []
        self.cur_min = None

    def push(self, val: int) -> None:
        if self.cur_min is None or self.cur_min >= val:
            x = val
            y = self.cur_min
            if y is not None and y >= val:
                val_to_push = 2*x - y
                self.cur_min = val
                self.main_stack.append(val_to_push)
                return
            else:
                self.cur_min = val
        self.main_stack.append(val)

    def pop(self) -> None:
        if len(self.main_stack) == 0:
            return None
        
        val = self.main_stack.pop(-1)
        if val <= self.cur_min:
            new_min = 2*self.cur_min - val
                 
            val_to_return = self.cur_min
            self.cur_min = new_min
            return val_to_return


    def top(self) -> int:
        if self.main_stack[-1] < self.cur_min:
            return self.cur_min
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.cur_min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
ops =  ["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
args = [[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]

# ops = ["MinStack","push","push","push","getMin","pop","top","getMin"]
# args = [[],[5],[2],[1],[],[],[],[]]

# ops = ["MinStack","push","push","push","getMin","pop","top","getMin"]
# args = [[],[-2],[0],[-3],[],[],[],[]]

ins = None
result = []
for i, o in enumerate(ops):
    arg = args[i]
    if o == 'MinStack':
        ins = MinStack()
        result.append(None)
    if o == 'push':
        ins.push(*arg)
        result.append(None)
    if o == 'pop':
        val = ins.pop()
        result.append(val)
    if o == 'top':
        val = ins.top()
        result.append(val)
    if o == 'getMin':
        val = ins.getMin()
        result.append(val)
print(result)
