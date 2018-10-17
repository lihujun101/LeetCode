from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_count = 0
        count = 0
        s_dict = set()
        s_queue = deque()
        for i in range(len(s)):

            if s[i] in s_dict:
                if max_count < count:
                    max_count = count
                while True:
                    count -= 1
                    s1 = s_queue.popleft()
                    s_dict.remove(s1)
                    if s1 == s[i]:
                        break
            s_dict.add(s[i])
            s_queue.append(s[i])
            count += 1

        if max_count < count:
            max_count = count
        return max_count


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("bbbbb"))
