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

@pytest.mark.parametrize("word, expected", testCases)
def testSolution(word, expected):
    result = S.detectCapitalUse(word)
    assert result == expected
