class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s = list(s)
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return ''.join(s)



# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         vowelsList = [vowel for vowel in s if vowel in "aeiouAEIOU"]
#         vowelsList.reverse()
#         strList = list(s)
#         for i in range(len(strList)):
#             if strList[i] in "aeiouAEIOU":
#                 strList[i] = vowelsList[0]
#                 vowelsList.pop(0)
#         return "".join(strList)
        