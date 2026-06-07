from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s)<len(t):
            return ""
        dictT=Counter(t)
        required=len(dictT)
        formed=0
        left,right=0,0
        windowT={}
        ans=float("inf"),None,None

        while right<len(s):
            char=s[right]
            windowT[char]=windowT.get(char,0)+1

            if char in dictT and dictT[char]==windowT[char]:
                formed+=1
            while left<=right and formed==required:
                char=s[left]
                if right-left+1<ans[0]:
                    ans=(right-left+1,left,right)
                windowT[char]-=1
                if char in dictT and windowT[char]<dictT[char]:
                    formed-=1
                left+=1
            right+=1
        return "" if ans[0]==float('inf') else s[ans[1]:ans[2]+1]