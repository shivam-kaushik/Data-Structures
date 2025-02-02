class Solution:
    def maxDifference(self, s: str) -> int:
    
        freq = Counter(s)
        
        even_freq = [f for f in freq.values() if f % 2 == 0]
        odd_freq = [f for f in freq.values() if f % 2 != 0]
        
        if not even_freq or not odd_freq:
            return 0
        
        max_odd = max(odd_freq)
        min_even = min(even_freq)
        
        return max_odd - min_even©leetcode