
class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        signs = {'+','-','/','*'}
        for token in tokens:
            if token not in signs:
                stack.append(token)
            else:
                first = stack.pop()
                second = stack.pop()
                if token == "+":
                    token = int(int(second) + int(first))
                elif token == "-":
                    token = int(int(second) - int(first))
                elif token == "*":
                    token = int(int(second) * int(first))
                elif token == "/":
                    token = int(int(second) / int(first))
                stack.append(token)
        return int(stack.pop())

if __name__ == '__main__':
    s = Solution()
    s1 = s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
    print(s1)