def is_int(s):
    try: 
        int(s)
    except ValueError:
        return False
    else:
        return True

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for n in tokens:
            if is_int(n):
                stack.append(int(n))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                if n == '+':
                    stack.append(n1+n2)
                elif n == '-':
                    stack.append(n1-n2)
                elif n == '*':
                    stack.append(n1*n2)
                elif n == '/':
                    stack.append(int(n1/n2))
            print(stack)
        return stack[0]

        