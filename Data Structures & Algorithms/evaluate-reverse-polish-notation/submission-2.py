class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']

        stack = []
        for token in tokens:
            if token in operators:
                second = stack.pop()
                first = stack.pop()
                if token == '+':
                    stack.append(int(first) + int(second))
                elif token == '-':
                    stack.append(int(first) - int(second))
                elif token == '*':
                    stack.append(int(first) * int(second))
                elif token == '/':
                    stack.append(int(int(first) / int(second)))
            else:
                stack.append(token)
        return int(stack[-1])
