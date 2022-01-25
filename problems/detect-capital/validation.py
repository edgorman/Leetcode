import pytest

from solution import Solution
S = Solution()

testCases = [
    ("USA", True),
    ("FlaG", False),
    ("leetcode", True),
    ("a", True),
    ("A", True),
    ("Aa", True),
    ("aA", False),
]

@pytest.mark.parametrize("input, expected", testCases)
def testSolution(input, expected):
    result = S.detectCapitalUse(input)
    assert result == expected
