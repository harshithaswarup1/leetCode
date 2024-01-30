class Solution(object):
    def singleNumber(self, nums):
        unique_elements= []
        for num in nums:
            if int(nums.count(num)) == int(1):
                unique_elements.append(num)
        return unique_elements
                
solution = Solution()
result = solution.singleNumber([4,1,2,1,2])