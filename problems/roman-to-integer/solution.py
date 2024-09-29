class Solution:
    def romanToInt(self, s: str) -> int:
        lookup = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        index = 0
        answer = 0

        while index < len(s):
            letter = s[index]
            value = lookup[letter]

            if index < len(s) - 1:
                next_letter = s[index + 1]
                next_value = lookup[next_letter]

                if next_value > value:
                    answer += next_value - value
                    index += 2
                    continue
            
            answer += value
            index += 1
        
        return answer


inputs = [
    {
        "s": "III"
    },
    {
        "s": "LVIII"
    },
    {
        "s": "MCMXCIV"
    }
]

solution = Solution()

for input in inputs:
    print("input", input, "answer:", solution.romanToInt(**input))
