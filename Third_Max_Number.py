class Solution(object):
    def thirdMax(self,nums):
        unique_nums = sorted(set(nums), reverse=True)
        if len(unique_nums) >= 3:
            return unique_nums[2]
        else:
            return unique_nums[0]
solution = Solution()
result = solution.thirdMax([2,2,3,1])