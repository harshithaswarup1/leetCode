class Solution(object):
    def summaryRanges(self, nums):
        if nums == []:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]

        start = nums[0]
        end = nums[0]
        result = []
        final_result = []

        for num in nums[1:]:
            if num == end + 1:
                end = num
            else:
                result.append([start, end])
                start = end = num
        result.append([start, end])

        for values in result:
            if values[0] == values[1]:
                final_result.append(str(values[0]))
            else:
                final_result.append(str(values[0]) + "->" + str(values[1]))

        return final_result

solution = Solution()
result = solution.summaryRanges([1, 3])