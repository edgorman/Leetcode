class Solution(object):
    def run(self, field: str) -> str:
        return field


inputs = [
    {
        "field": "value"
    }
]

solution = Solution()

for input in inputs:
    print("input", input, "answer:", solution.run(**input))
