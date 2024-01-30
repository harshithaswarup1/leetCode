class Solution(object):
    def pivotIndex(self, nums):
        if len(nums) == 0:
            return -1
        else:
            for i in range(len(nums)):
                if sum(nums[:i]) == sum(nums[i + 1:]):
                    return i
            return -1

solution = Solution()
result = solution.pivotIndex([-2, 1, -1])