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


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[n]
    

# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         words = set(wordDict)
#         wordBreakCurr = [False for i in range(len(s))]
#         for i in range(len(s)):
#             if s[:i+1] in words:
#                 wordBreakCurr[i] = True
#                 continue
#             for j in range(i): 
#                 if wordBreakCurr[j] == True and s[j+1:i+1] in words:
#                     wordBreakCurr[i] = True
#                     continue
#         return wordBreakCurr[len(s)-1]