class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        rows_freq = collections.Counter(tuple(rows) for rows in grid)
        columns = zip(*grid)
        result = sum(rows_freq[cols] for cols in columns)
        return result

# class Solution:
#     def equalPairs(self, grid: List[List[int]]) -> int:
#         rows = grid
#         columns = list(zip(*grid))
#         count = 0
#         for row in rows:
#             for col in columns:
#                 if tuple(row) == col:
#                     count += 1
#         return count