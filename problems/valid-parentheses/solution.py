class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mappings = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for letter in s :
            if letter in mappings.keys():
                stack.append(letter)
            elif len(stack) > 0:
                popped = stack.pop()
                if mappings[popped] != letter:
                    return False
            else:
                return False

        return len(stack) == 0


inputs = [
    {
        "s": "()"
    },
    {
        "s": "()[]{}"
    },
    {
        "s": "(]"
    },
    {
        "s": "([])"
    },
    {
        "s": "]"
    }
]

solution = Solution()

for input in inputs:
    print("input", input, "answer:", solution.isValid(**input))
