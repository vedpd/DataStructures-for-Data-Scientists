class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 1:
            return False
        
        temp_dict={}

        for index, value in enumerate(nums):
            if value in temp_dict:
                return [temp_dict[value],index]
            
            else:
                temp_dict[target-value] = index