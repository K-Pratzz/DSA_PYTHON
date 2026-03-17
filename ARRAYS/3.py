class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet=set()
        l=0
        maxl=0
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[right])
            maxl=max(maxl,right-l+1)
        return maxl