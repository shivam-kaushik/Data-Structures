class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for i in range(len(strs)):
            key = tuple(sorted(strs[i]))
            if key in hashmap.keys():
                hashmap[key].append(strs[i])
            else:
                hashmap[key] = [strs[i]]
        
        return list(hashmap.values())