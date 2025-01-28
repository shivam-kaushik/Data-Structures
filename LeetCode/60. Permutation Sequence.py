class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math
        
        numbers = list(range(1, n + 1))
        
        result = []
        
        k -= 1
        
        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)
            index = k // fact
            result.append(str(numbers.pop(index)))
            k %= fact
        
        return ''.join(result)


# class Solution:
#     def getPermutation(self, n: int, k: int) -> str:

#         lst = [i for i in range(1, n+1)]

#         all_perms = list(permutations(lst))
#         all_perms.sort()
#         kth_perm = all_perms[k-1]
#         return ''.join(map(str, kth_perm))