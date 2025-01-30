class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(current, open, close, result):
            if len(current) == 2 * n:
                result.append(current)
                return
            
            if open < n:
                backtrack(current + '(', open + 1, close, result)
            
            if close < open:
                backtrack(current + ')', open, close + 1, result)
        
        result = []
        backtrack("", 0, 0, result)
        return result



class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []
        def generate(opened, closed):
            if opened == closed == n:
                result.append(''.join(stack))
            if opened < n:
                stack.append('(')
                generate(opened + 1, closed)
                stack.pop()
            if closed < opened:
                stack.append(')')
                generate(opened, closed + 1)
                stack.pop()
        generate(0, 0)
        return result