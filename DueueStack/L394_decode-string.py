class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack_left = []
        i = 0
        while i < len(s):
            if s[i] == '[':
                stack_left.append(i)
            elif s[i] == ']':
                left = stack_left.pop()
                right = i
                mid = ""

                num_start, num_end = left - 1, left
                # 去寻找[前面的最大数字
                while num_start > 0 and s[num_start - 1] in '0123456789':
                    num_start -= 1
                # 字符串转为整数
                times = int(s[num_start:num_end])

                for j in range(times):
                    mid = mid + s[left + 1:right]
                s = s[0:num_start] + mid + s[right + 1:]
                stack_left = []
                i = 0
            i += 1
        return s


if __name__ == '__main__':
    ss = "100[abc]"
    s = Solution()
    s1 = s.decodeString(ss)
    print(s1)
