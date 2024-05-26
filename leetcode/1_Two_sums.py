def twoSum(
    nums, target
):

    sorted_tuples = sorted(enumerate(nums), key=lambda x:x[1])
    i = 0
    j = len(nums) - 1

    while i < j:
        if sorted_tuples[i][1] + sorted_tuples[j][1] == target:
            return [sorted_tuples[i][0], sorted_tuples[j][0]]
        
        elif target - sorted_tuples[j][1] < sorted_tuples[i][1]:
            j -= 1
        else:
            i += 1

nums = [1, 2, 4, 4, 5, 13, 88]
target = 8

print(twoSum(nums, target))




# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         nums = sorted(enumerate(nums), key=lambda x:x[1])
#         i = 0
#         j = len(nums) - 1

#         while i < j:
#             if nums[i][1] + nums[j][1] == target:
#                 return [nums[i][0], nums[j][0]]
            
#             elif target - nums[j][1] < nums[i][1]:
#                 j -= 1
#             else:
#                 i += 1
        