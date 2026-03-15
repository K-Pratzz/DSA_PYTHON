class Solution:
    def isPalindrome(self, s: str) -> bool:
        isans=False
        s="".join(char for char in s if char.isalnum())
        s=s.lower()
        rev=s[::-1]
        if s==rev:
            isans=True
        return isans