class Solution(object):
    def singleNumber(self, nums):
        for num in nums:
            if int(nums.count(num)) == 1:
                return num
                
solution = Solution()
result = solution.singleNumber([4,1,2,1,2])