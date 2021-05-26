#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start

# This approach works on the following concept :
# a. 1st element would always be unique
# b. hence to identify next unique element start from index= 1
# c. compare value of every element with next element
#    if comparison is equal- do nothing and move ahead
#    if comparison is unequal - then the value at index position is updated with one value ahead
#    since value at index has been updated, move index forward
# d. Index is being used to track the unique values and utilizing it to swap and track index till
#    values are unique.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size= len(nums)
        index=1

        for i in range(len(nums)-1):
            if(nums[i] != nums[i+1]):
                nums[index]= nums[i+1]
                index+=1
        
        return index



        
# @lc code=end

