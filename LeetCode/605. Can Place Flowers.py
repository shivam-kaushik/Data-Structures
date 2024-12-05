class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1 
                if n == 0:
                    return True
        
        return n <= 0

# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         f = [0] + flowerbed + [0]
#         for i in range(1, len(f) - 1):
#             if f[i - 1] == 0 and f[i] == 0 and f[i+1] == 0:
#                 f[i] = 1
#                 n -= 1

#         return n <= 0