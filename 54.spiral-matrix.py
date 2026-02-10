class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []

        ret = []
        while matrix and matrix[0]:
            # 1) Top row
            ret += matrix.pop(0)

            # 2) Right column
            if matrix and matrix[0]:
                # only pop from rows that are non-empty
                for row in matrix:
                    if row:              # guard in case row is empty
                        ret.append(row.pop())

            # Remove any now-empty rows to keep checks clean
            matrix = [row for row in matrix if row]

            # 3) Bottom row (reversed)
            if matrix:
                ret += matrix.pop()[::-1]

            # 4) Left column (bottom to top)
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    if row:              # guard again
                        ret.append(row.pop(0))

            # Clean any empty rows again
            matrix = [row for row in matrix if row]

        return ret