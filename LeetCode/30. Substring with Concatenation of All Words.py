from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
            
        word_len = len(words[0])
        window_len = word_len * len(words)
        
        if len(s) < window_len:
            return []
            
        word_count = Counter(words)
        result = []
        
        for start in range(word_len):
            left = start
            curr_count = Counter()
            words_used = 0
            for right in range(start, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]
                
                if word in word_count:
                    curr_count[word] += 1
                    words_used += 1
                    
                    while curr_count[word] > word_count[word]:
                        curr_count[s[left:left + word_len]] -= 1
                        words_used -= 1
                        left += word_len
                        
                    if words_used == len(words):
                        result.append(left)
                        curr_count[s[left:left + word_len]] -= 1
                        words_used -= 1
                        left += word_len
                else:
                    curr_count.clear()
                    words_used = 0
                    left = right + word_len
                    
        return result