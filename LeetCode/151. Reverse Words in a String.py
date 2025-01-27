class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(list(reversed(s.split())))


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split()
        words.reverse()
        return ' '.join(words)