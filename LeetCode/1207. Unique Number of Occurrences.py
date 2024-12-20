class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for x in arr:
            freq[x] = freq.get(x, 0) + 1

        return len(freq) == len(set(freq.values()))



# class Solution:
#     def uniqueOccurrences(self, arr: List[int]) -> bool:
#         freq_dict = {}
#         for num in arr:
#             if num in freq_dict:
#                 freq_dict[num] += 1
#             else:
#                 freq_dict[num] = 1

#         occurrence_counts = []
#         for count in freq_dict.values():
#             if count in occurrence_counts:
#                 return False
#             occurrence_counts.append(count)

#         return True
