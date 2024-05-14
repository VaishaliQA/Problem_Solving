class MyStack:
    def __init__(self):
        self.mystack =deque()
        
    def push(self, x: int) -> None:
        self.mystack.append(x)
        
    def pop(self) -> int:
        for i in range(len(self.mystack)-1):
            self.push(self.mystack.popleft())
        return self.mystack.popleft()
        
    def top(self) -> int:
        return self.mystack[-1]
        
    def empty(self) -> bool:
        if(len(self.mystack)==0):
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()