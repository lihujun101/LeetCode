class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        palindrome_container = []
        for idx in range(0, length):
            n_list = []
            # 'aba'类型
            if s[idx:idx + 2] == s[idx:idx + 2][::-1]:
                n_list.append(2)
            # 'bb'类型
            if s[idx:idx + 3] == s[idx:idx + 3][::-1]:
                n_list.append(3)
            while n_list:
                n = n_list.pop()
                min_t = min(idx, length - idx - n)
                j = 0
                while j < min_t:
                    if s[idx - j] == s[idx + n - 1 + j]:
                        j += 1
                        if s[idx - j] == s[idx + n - 1 + j]:
                            continue
                        else:
                            j -= 1
                            break
                    else:
                        j -= 1
                        break
                palindrome_container.append(s[idx - j: idx + n + j])


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
    m = "ccc"
    m1 = Solution().longestPalindrome(m)
    print(m1)
