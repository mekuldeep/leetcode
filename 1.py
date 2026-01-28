# 1. Two Sum
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

class Solution():
    def twoSum(self, nums, target):
        for i, n in enumerate(nums): 
            if n >= target:
                continue
            for j in range(i+1, len(nums)):
                if (n + nums[j] == target):
                    return [i, j]
                
    # def twoSum(self, nums, target):
    #     seen = {}        
    #     for i, n in enumerate(nums):
    #         diff = target - n
    #         print(diff in seen)
    #         if diff in seen:
    #             print([seen[diff], i])
    #             return [seen[diff], i]
    #         print(seen)
    #         seen[n] = i

    
nums = [2,7,11,15]
target = 9
obj = Solution()
result = obj.twoSum(nums , target)
print('output is: ', result)


# Approch 2
# def findSum(nums, target):
#     for i, n in enumerate(nums):
#         nextVal = target - n
#         if nextVal in nums:
#             return([i, nums.index(nextVal)])
    
# nums = [1,3,4,5]
# target = 7
# result = findSum(nums, target)
# print(result)

        