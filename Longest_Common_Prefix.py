class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        min_length = min(strs, key=len)
        common_prefix = []

        for i in range(len(min_length)):
            for word in strs:
                if i < len(word) and word[i] == min_length[i]:
                    continue
                else:
                    return ''.join(common_prefix)

            common_prefix.append(min_length[i])

        return ''.join(common_prefix)

solution = Solution()
result = solution.longestCommonPrefix(["reflower", "flow", "flight"])