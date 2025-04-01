class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for i in range(0, len(nums)):
            if nums[i] in hashset:
                return [hashset[nums[i]], i]
            hashset[target-nums[i]] = i
        return -1

        