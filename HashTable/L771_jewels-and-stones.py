class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        J_set = set()
        count = 0
        for j in J:
            J_set.add(j)
        for s in S:
            if s in J_set:
                count += 1
        return count
