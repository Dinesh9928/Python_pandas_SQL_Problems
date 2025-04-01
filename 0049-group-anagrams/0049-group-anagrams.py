class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for i in strs:
            if tuple(sorted(i)) in hmap:
                hmap[tuple(sorted(i))].append(i)
            else:
                hmap[tuple(sorted(i))] = [i]

        res = hmap.values()
        return list(res)
        