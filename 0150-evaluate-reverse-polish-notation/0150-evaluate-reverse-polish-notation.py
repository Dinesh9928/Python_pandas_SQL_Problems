class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in ("+", "-", "*", "/"):
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                if i == "+":
                    stack.append(b + a)
                elif i == "-":
                    stack.append(b - a)
                elif i == "/":
                    stack.append(int(b / a))
                elif i == "*":
                    stack.append(b*a)
        
        return stack[-1]

            
        