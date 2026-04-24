
import math
class Solution:
    def minimizedMaximum( n, quantities) -> int:
        low,high=1,max(quantities)
        ans=high
        while low<=high:
            mid=(low+high)//2
            stores=0
            for q in quantities:
                stores+=math.ceil(q/mid)
            if stores<=n:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans