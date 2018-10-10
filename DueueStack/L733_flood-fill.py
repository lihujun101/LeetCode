class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        high = len(image) - 1
        length = len(image[0]) - 1
        finded = set()
        modified = [(sr, sc)]
        finded.add((sr, sc))
        color = image[sr][sc]
        while modified:
            i, j = modified.pop()
            image[i][j] = newColor
            if i > 0:
                if image[i - 1][j] == color and (i - 1, j) not in finded:
                    finded.add((i - 1, j))
                    modified.append((i - 1, j))

            if i < high:
                if image[i + 1][j] == color and (i + 1, j) not in finded:
                    finded.add((i + 1, j))
                    modified.append((i + 1, j))

            if j < length:
                if image[i][j + 1] == color and (i, j + 1) not in finded:
                    finded.add((i, j + 1))
                    modified.append((i, j + 1))
            if j > 0:
                if image[i][j - 1] == color and (i, j - 1) not in finded:
                    finded.add((i, j - 1))
                    modified.append((i, j - 1))
        return image


if __name__ == '__main__':
    s = Solution()
    r = s.floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, newColor=2)
    print(r)
