class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        duplicate=set()
        ans=[]
        n=len(grid)
        for i in range(n):
            for j in range(n):
                val=grid[i][j]
                if val in duplicate:
                    ans.append(val)
                else:
                    duplicate.add(val)

        for x in range(1,(n*n)+1):
            if x not in duplicate:
                ans.append(x)
                break
        return ans
        