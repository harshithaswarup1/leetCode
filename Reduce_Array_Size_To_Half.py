from collections import Counter

class Solution(object):
    def minSetSize(self, arr):
        count_dict = Counter(arr)
        sorted_counts = sorted(count_dict.values(), reverse=True)

        total_elements = len(arr)
        target_size = total_elements // 2
        current_size = 0
        sets_count = 0

        for count in sorted_counts:
            current_size += count
            sets_count += 1

            if current_size >= target_size:
                return sets_count

solution = Solution()
result = solution.minSetSize([1, 2, 3, 4, 5, 6, 7, 8, 9])