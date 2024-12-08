class Solution:
    def compress(self, chars: List[str]) -> int:
        write, count = 0, 1 
        
        for i in range(1, len(chars) + 1):
            if i < len(chars) and chars[i] == chars[i - 1]: 
                count += 1
            else:
                chars[write] = chars[i - 1]  
                write += 1
                if count > 1: 
                    for c in str(count):  
                        chars[write] = c
                        write += 1
                count = 1  
        
        return write 
