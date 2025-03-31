class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = [0]*2
        for i in range(0, len(nums) -1):
            remain = target - nums[i]
            for j in range(i+1, len(nums)):
                if remain == nums[j]:
                    res[0] = i
                    res[1] = j
                    return res
        return -1

        