class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return ""
        m = ""
        string_list = []
        for i in s:
            if i != " ":
                m = m + i
            elif i == " " and m != "":
                string_list.append(m)
                m = ""
        if m != "":
            string_list.append(m)
        i, j = 0, len(string_list) - 1
        while i < j:
            string_list[i], string_list[j] = string_list[j], string_list[i]
            i += 1
            j -= 1

        return ' '.join(string_list)





if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("the sky is blue   "))
