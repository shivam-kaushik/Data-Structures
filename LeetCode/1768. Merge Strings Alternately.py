class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        result = []
        
        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            i += 1
            result.append(word2[j])
            j += 1
        if len(word1)> len(word2):
            result.append(word1[i:])
        else:
            result.append(word2[j:])
        return ''.join(result)