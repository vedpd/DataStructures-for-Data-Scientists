class SparseVector:
    def __init__(self, nums: List[int]):

        #define the hashmap
        self.hm={}
        for i, n in enumerate(nums):
            if n is not 0:
                self.hm[i] = n
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res =0

        for i,v in vec.hm.items(): #access the vector's hashmap's items to get the key and value
            if i in self.hm:
                 res += v * self.hm[i]
        
        return res


        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)



# \U0001f539 __init__ method
# This constructor initializes the vector.

# It creates a dictionary (self.hm) to store only the non-zero values of the vector.

# The keys are indices and values are the non-zero elements at those indices.

# Example:
# If nums = [1, 0, 0, 2, 3], then

# python
# Copy
# Edit
# self.hm = {
#     0: 1,
#     3: 2,
#     4: 3
# }
# This saves space by ignoring the zero entries.

# python
# Copy
# Edit
# def dotProduct(self, vec: 'SparseVector') -> int:
#     res = 0
#     for i, v in vec.hm.items():
#         if i in self.hm:
#             res += v * self.hm[i]
#     return res
# \U0001f539 dotProduct method
# This method computes the dot product between:

# self → the current sparse vector (already stored in self.hm)

# vec → another SparseVector object (also using a dictionary internally)

# \U0001f9e0 Logic:
# Loop through each (index, value) pair in the other vector’s dictionary.

# If that index is also in self.hm, it means both vectors have non-zero values at that position.

# Multiply the two values and accumulate the result.

# Why is this efficient?
# You only compute dot products for positions that are non-zero in both vectors, saving time on zero multiplications.

# ✅ Full Example Walkthrough:
# python
# Copy
# Edit
# nums1 = [1, 0, 0, 2, 3]
# nums2 = [0, 3, 0, 4, 0]

# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)

# v1.hm = { 0: 1, 3: 2, 4: 3 }
# v2.hm = { 1: 3, 3: 4 }

# # dot product
# # Only index 3 is common
# # v1[3] * v2[3] = 2 * 4 = 8

# Result = 8