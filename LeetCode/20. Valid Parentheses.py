class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for i in range(len(s)):
            if s[i] in hashmap.values():
                stack.append(s[i])
            elif s[i] in hashmap.keys():
                if stack and hashmap[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return (len(stack) == 0)