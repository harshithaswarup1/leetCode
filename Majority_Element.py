class Solution(object):
    def majorityElement(self, nums):
        element_count = {}
        for item in nums:
            if item in element_count:
                element_count[item] += 1
            else:
                element_count[item] = 1
        max_value = max(element_count, key=element_count.get)
        return max_value

solution = Solution()
result = solution.majorityElement([3,2,3])
result = solution.majorityElement([2,2,1,1,1,2,2])