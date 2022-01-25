# 941. Valid Mountain Array

Difficulty: ```Easy```

Source: https://leetcode.com/problems/valid-mountain-array/

## Description

Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

```
arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
```

Example 1:
```
Input: arr = [2,1]
Output: false
```

Example 2:
```
Input: arr = [3,5,5]
Output: false
```

Example 3:
```
Input: arr = [0,3,2,1]
Output: true
```

Constraints:
```
1 <= arr.length <= 104
0 <= arr[i] <= 104
```

## Explanation

__Overview:__

This challenge was difficult initially for being able to produce a clean and readable solution that wasn't heavily reliant on flags for knowing the current state of the mountain array. In the end the code was partioned into two logical sections where the array would be incresing and decreasing to handle this, alongside if statements to confirm the mountain array was valid up to this point.

__Complexity:__

The time complexity is O(n) since we check every value once in a linear fashion.

The space complexity is O(1) since we have a fixed amount of memory to store our variables.
