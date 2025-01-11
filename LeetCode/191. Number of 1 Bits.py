class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = "{0:b}".format(int(n))

        return binary.count('1')
    

# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         cnt = 0
#         while n > 0:
#             if n % 2 == 1:
#                 cnt += 1
#             n = n //2
#         return cnt