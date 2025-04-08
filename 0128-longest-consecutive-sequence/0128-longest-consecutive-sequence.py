class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0
        for i in numSet:
            if i-1 not in numSet: # it's the head
                length = 0
                while(i+length in numSet):
                    length += 1
                maxLen = max(maxLen, length)
        return maxLen
            
        

        