class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        lst = [i for i in range(1, n+1)]

        all_perms = list(permutations(lst))
        all_perms.sort()
        kth_perm = all_perms[k-1]
        return ''.join(map(str, kth_perm))