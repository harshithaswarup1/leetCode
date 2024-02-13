class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        i = 0

        # Iterate through the array
        for j in range(1, len(nums)):
            # If the current element is different from the previous one, if the elements are
            #unique, inc the value of "i" by 1
            if nums[j] != nums[i]:
                # Move the pointer
                i += 1
                # Update the array in-place
                nums[i] = nums[j]

        # The length of the modified array is (i + 1)
        return i + 1


solution = Solution()
result = solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])

