class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_idx = len(s) - 1
        first_idx = 0
        list_s = list(s)
        while first_idx <= last_idx:
            list_s[first_idx], list_s[last_idx] = list_s[last_idx], list_s[first_idx]
            first_idx += 1
            last_idx -= 1
        return ''.join(list_s)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseString("A man, a plan, a canal: Panama"))
