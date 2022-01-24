class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        # If word is length 1, word is valid
        if len(word) == 1:
            return True
        
        # If the first two letters are uppercase
        if word[0].isupper() and word[1].isupper():
            # Check remaining letters are uppercase
            for letter in word[2:]:
                if not letter.isupper():
                    return False
        
        # Else the remaining letters must be lowercase
        else:
            # Check remaining letters are lowercase
            for letter in word[1:]:
                if not letter.islower():
                    return False
        
        # Word must be valid, return true
        return True
