class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)/3
        majority_elements = []
        element_count = {}
        for item in nums:
            if item in element_count:
                element_count[item] += 1
            else:
                element_count[item] = 1
        for key,val in element_count.items():
            if val > n:
                majority_elements.append(key)
        return majority_elements
                
solution = Solution()
result = solution.majorityElement([3,2,3])
result = solution.majorityElement([1])
result = solution.majorityElement([1,2])