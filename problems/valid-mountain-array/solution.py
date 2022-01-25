class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        # Return false if array length is less than 3
        if len(arr) < 3:
            return False
        
        # Store which position of the array we are at
        i = 0
        
        # Walk up the mountain
        while i < len(arr) - 1:
            # Return false if values are equal
            if arr[i] == arr[i + 1]:
                return False
            # Increment index if values are ascending
            elif arr[i] < arr[i + 1]:
                i += 1
            # Break loop if values are descending
            else:
                break
        
        # Return false if index is at start or end of array
        if i == 0 or i == len(arr) - 1:
            return False
        
        # Walk down mountain
        while i < len(arr) - 1:
            # Return false if values are equal
            if arr[i] == arr[i + 1]:
                return False
            # Increment index if values are descending
            elif arr[i] > arr[i + 1]:
                i += 1
            # Return false if values are ascending
            else:
                return False
        
        # Return true if index is at end of array
        return i == len(arr) - 1
