class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set(nums)
        return len(hashset) < len(nums)
        # freq = set() # using set
        # for num in nums: 
        #     if num in freq: 
        #         return True
        #     freq.add(num)
        # return False
        