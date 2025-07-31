class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
    
        else:
            counter= {}

            for elem in nums:
                if elem in counter:
                    return True
                else:
                    counter[elem] = 1      

        return False
            