from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        row = len(matrix)
        col = len(matrix[0])

        rowstart = 0
        rowend = row - 1
        strtcol = 0
        endcol = col - 1

        while rowstart <= rowend and strtcol <= endcol:
            for i in range(strtcol, endcol + 1):
                ans.append(matrix[rowstart][i])
            rowstart += 1

            for i in range(rowstart, rowend + 1):
                ans.append(matrix[i][endcol])
            endcol -= 1

            if rowstart <= rowend:
                for i in range(endcol, strtcol - 1, -1):
                    ans.append(matrix[rowend][i])
            rowend -= 1
            
            if strtcol <= endcol:
                for i in range(rowend, rowstart - 1, -1):
                    ans.append(matrix[i][strtcol])
            strtcol += 1

        return ans