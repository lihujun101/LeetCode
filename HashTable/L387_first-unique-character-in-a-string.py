class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_dict = {}
        for idx, key in enumerate(s):
            if key not in char_dict:
                char_dict[key] = [idx, 1]
            else:
                char_dict[key][1] += 1
        min = len(s)
        for key in char_dict:
            if char_dict[key][1] == 1:
                if min > char_dict[key][0]:
                    min = char_dict[key][0]
        if min == len(s):
            return -1
        else:
            return min

if __name__ == '__main__':
    s= Solution()
    print(s.firstUniqChar(s="aa"))