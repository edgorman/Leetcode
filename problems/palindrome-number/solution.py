class Solution(object):
    def isPalindrome(self, value: str) -> str:
        return str(value) == str(value)[::-1]


inputs = [
    {
        "value": 121
    },
    {
        "value": -121
    },
    {
        "value": 10
    }
]

solution = Solution()

for input in inputs:
    print("input", input, "answer:", solution.isPalindrome(**input))
