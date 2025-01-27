class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = {}

        def helper(s):
            if s in memo:
                return memo[s]
            if not s:
                return True
            for word in wordSet:
                if s.startswith(word):
                    if helper(s[len(word):]):
                        memo[s] = True
                        return True
            memo[s] = False
            return False

        return helper(s)