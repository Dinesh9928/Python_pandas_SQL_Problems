class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = [0]* 1000
        for i in range(0, len(nums)):
            if(freq[nums[i]] != 0):
                return True
            else:
                freq[nums[i]] = 1
        return False
        