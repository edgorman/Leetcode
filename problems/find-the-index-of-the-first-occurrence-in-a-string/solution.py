class Solution(object):
    # def strStr(self, haystack: str, needle: str) -> int:
    #     try:
    #         return haystack.index(needle)
    #     except ValueError:
    #         return -1

    def strStr(self, haystack: str, needle: str) -> int:
        for left in range(0, len(haystack) - len(needle) + 1):
            if haystack[left:left+len(needle)] == needle:
                return left

        return -1


inputs = [
    {
        "haystack": "sadbutsad",
        "needle": "sad"
    },
    {
        "haystack": "leetcode",
        "needle": "leeto"
    }
]

solution = Solution()

for input in inputs:
    print("input", input, "answer:", solution.strStr(**input))
