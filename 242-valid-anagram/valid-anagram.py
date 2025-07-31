class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If length of strings are unequal
        if len(s) != len(t):
            return False

        else:
            counter={}

            # updating the counter dictionary from string 1
            for char in s :

                if char in counter:
                    counter[char] += 1
                else:
                    counter[char] = 1
            
            # removing elements from counter dictionary based on        presence of charater in counter

            for char in t:
                if char in counter:
                    counter[char] -= 1
                
                else:
                    return False
            
            # validating if counter post updates is having any non zero value -> returns False
            if any(value != 0 for value in counter.values()):
                return False
            
            # if all values are 0, then return True
            else:
                return True

            