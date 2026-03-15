class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        word=s.split()
        word=word[::-1]
        s=" ".join(word)
        return s