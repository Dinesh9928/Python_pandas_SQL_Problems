class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for i in nums:
            dict[i] = dict.get(i, 0) + 1
        
        sortedByValueList = [key for key, value in sorted(dict.items(), key = lambda x: x[1], reverse = True )]

        return sortedByValueList[:k]