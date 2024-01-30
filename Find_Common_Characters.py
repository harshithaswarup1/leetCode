from collections import Counter

class Solution(object):
    def commonChars(self, words):
        counters = [Counter(word) for word in words]
        common_chars_counter = counters[0]
        for counter in counters[1:]:
            common_chars_counter &= counter
        common_chars_list = list(common_chars_counter.elements())
        return common_chars_list
solution = Solution()
result = solution.commonChars(["bella","label","roller"])