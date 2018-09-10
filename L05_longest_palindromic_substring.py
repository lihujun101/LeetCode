class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        palindrome_container = []
        for idx in range(0, length):
            # 正序一个个去找index的位置
            for idx_reverse in range(length - 1, idx, -1):
                # 逆序去找到s[idx] == s[idx_rerverse]的位置
                if s[idx] == s[idx_reverse] and idx != idx_reverse:
                    # 找到后再细致观察是否是回文，如果是回文就追加至列表
                    idx01, idx_reverse01 = idx, idx_reverse
                    s1 = s[idx:idx_reverse + 1]
                    if s1 == s[::-1]:
                        print(s1)
                        palindrome_container.append(s[idx:idx_reverse + 1])

                    # while s[idx01] == s[idx_reverse01]:
                    #     if idx_reverse01 - idx01 == 1 or idx_reverse01 - idx01 == 2:
                    #         palindrome_container.append(s[idx:idx_reverse + 1])
                    #         break
                    #     idx01 += 1
                    #     idx_reverse01 -= 1
                elif idx == idx_reverse:
                    break
        if s == "":
            return ""
        if palindrome_container == []:
            return s[0]
        max_length = 0
        longest_palindromic = ""
        for palindrome in palindrome_container:
            palindrome_length = len(palindrome)
            if max_length < palindrome_length:
                max_length = palindrome_length
                longest_palindromic = palindrome
        return longest_palindromic


if __name__ == '__main__':
    m = "aaabaaaa"
    m1 = Solution().longestPalindrome(m)
    print(m1)
