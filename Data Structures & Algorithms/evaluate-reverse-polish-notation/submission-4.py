class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "/", "*"}

        stack = []

        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))
            elif tokens[i] in operators:
                a = stack.pop()
                b = stack.pop()

                if tokens[i] == '+':
                    stack.append(a + b)
                elif tokens[i] == '*':
                    stack.append(a * b)
                elif tokens[i] == '-':
                    stack.append(b - a)
                else:
                    stack.append(int(b / a))
        return stack[0]
#stack -> -11,12,6,10