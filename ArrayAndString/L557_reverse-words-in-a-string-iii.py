class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        m = ""
        srting_list = []
        for i in s:
            if i != " ":
                m += i
            elif i == " " and m != "":
                srting_list.append(m[::-1])
                m = ""
        srting_list.append(m[::-1])
        return ' '.join(srting_list)

if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("Let's take LeetCode contest"))