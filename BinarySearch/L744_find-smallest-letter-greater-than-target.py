class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        idx = 0
        while idx <= len(letters) - 1:
            if letters[idx] > target:
                return letters[idx]
            else:
                idx += 1
        return letters[0]


if __name__ == '__main__':
    s = Solution()
    print(s.nextGreatestLetter(letters=["f", 'f', 'f', 'f', 'f', "j"], target='f'))
