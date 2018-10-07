from time import time


class Solution:
    # 原有做法，时间复杂度O(n^2)
    def dailyTemperatures1(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result.append(j - i)
                    break
                if j == len(temperatures) - 1 and temperatures[j] <= temperatures[i]:
                    result.append(0)
        result.append(0)

        return result

    # 新做法，用栈实现，倒序计算，时间复杂度O(n)
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        length = len(temperatures)
        result = [0] * length
        # stack记录位置，不能记录值，位置相减就是相差的天数
        stack = []
        for i in range(length - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            # stack == []
            if stack == []:
                stack.append(i)
            else:
                result[i] = stack[-1] - i
                stack.append(i)
        return result


if __name__ == '__main__':
    s = Solution()
    start_time = time()
    r = s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
    end_time = time()
    print(r)
    print(end_time - start_time)
