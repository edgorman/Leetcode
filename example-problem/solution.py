class Solution(object):
    def run(self, field: str) -> str:
        return field


inputs = [
    {
        "field": "value"
    }
]

solution = Solution()
results = []

for input in inputs:
    results.append(solution.run(**input))

print(results)
