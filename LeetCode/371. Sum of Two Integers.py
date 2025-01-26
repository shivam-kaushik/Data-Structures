class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        while b != 0:
            temp = (a & b) << 1
            a = a ^ b
            a &= mask
            b = temp & mask
        return a if a <= max_int else ~(a ^ mask)
    
    
# class Solution:
#     def getSum(self, a: int, b: int) -> int:
#         return add(a,b)
    

# SOLUTION IN JAVA

# class Solution {
#     public int getSum(int a, int b) {
#         if (b == 0) {
#             return a;
#         } else {
#             return getSum(a ^ b, (a & b) << 1);
#         }
#     }
# }