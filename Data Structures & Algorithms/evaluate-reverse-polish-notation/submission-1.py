class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for key in tokens:
            if key in "+-*/":
                b = int(stack.pop())
                a = int(stack.pop())
                if key == '+':
                    stack.append(a + b)
                elif key == '-':
                    stack.append(a - b)
                elif key == '*':
                    stack.append(a * b)
                elif key == '/':
                    stack.append(int(a / b))
            else:
                stack.append(int(key))
        return stack[-1]
            