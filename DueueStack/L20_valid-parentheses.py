class Solution:
    # 这道题实在做的复杂，看答案了
    def isValid(self, s):
        a = {')': '(', ']': '[', '}': '{'}
        stack = [None]
        for i in s:
            # stack = [None]为了避免stack[-1]报错
            if i in a and a[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 1




if __name__ == '__main__':
    s = Solution()
    r = s.isValid("(([])[]{})")  # (([]){})  、[) 、([)] 、()[]{}
    print(r)
