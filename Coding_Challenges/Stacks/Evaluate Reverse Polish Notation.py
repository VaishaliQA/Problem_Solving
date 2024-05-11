class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation =["+","-","*","/"]
        stack =[]
        res = 0
        if len(tokens)==1:
            return int(tokens[0])
        for op in tokens:
            if op in operation:
                res = eval(f'{stack[-2]} {op} {stack[-1]}')
                stack.pop()
                stack.pop()
                stack.append(int(res))
            else:
                stack.append(op)  
        return stack[0]   