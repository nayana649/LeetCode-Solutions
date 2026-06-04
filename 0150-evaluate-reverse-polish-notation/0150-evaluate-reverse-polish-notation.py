class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        
        for token in tokens:
            if token in operators:
                # Pop the right operand first, then the left operand
                b = stack.pop()
                a = stack.pop()
                
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    # int() truncates division towards zero in Python
                    stack.append(int(a / b))
            else:
                # Token is an operand, cast and push to stack
                stack.append(int(token))
                
        # The final remaining element is the total expression result
        return stack[0]