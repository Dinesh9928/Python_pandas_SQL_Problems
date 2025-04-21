class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        res = nums[0]

        while (left <= right):
            mid = (right + left)//2
            if(nums[mid] >= nums[left]):
                res = min(res, nums[left])
                left = mid + 1
            else:
                res = min(res, nums[mid])
                right = mid -1

        return res
    