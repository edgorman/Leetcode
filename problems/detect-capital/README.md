# 520. Detect Capital 

Difficulty: ```Easy```

Source: https://leetcode.com/problems/detect-capital/

## Description

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

Example 1:

```
Input: word = "USA"
Output: true
```

Example 2:
```
Input: word = "FlaG"
Output: false
```

Constraints:
```
1 <= word.length <= 100
word consists of lowercase and uppercase English letters.
```

## Explanation

__Overview:__

The problem of detecting capitals was a very simple one albeit with some tricky logic that would be simple to write incorrectly for an edge case. The solution required both an extensive test set to ensure all cases were accounted for, and an analysis of these cases to simplify the program logic and make it readable. 

__Complexity:__

The time complexity is O(n) since we check each character in the word linearly.

The space complexity is O(1) since we a fixed amount of memory to store our variables.