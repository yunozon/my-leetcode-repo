# Two sum
class Solution:
    def twoSum(self, nums, target):
        # brute force
        n = len(nums)
        ans = []
        for i in range(n-1):
            for j in range(i+1, n):
                print(f"{i} : i, j : {j}")
                sum = nums[i] + nums[j]
                if sum == target:
                    ans.append(i)
                    ans.append(j)
                    return ans
        return ans
    
    def twoSum2(self, nums, target):
        ans = []
        start_index = 0
        end_index = len(nums) - 1
        while True:
            sum = 0
            sum = nums[start_index] + nums[end_index]                
            
            if sum < 0:
                if sum > target:
                    start_index += 1
                    continue
                elif sum < target:
                    end_index -= 1
                    continue
                else:
                    ans.append(start_index)
                    ans.append(end_index)
                
                    return ans 
        
            else:
                if sum > target:
                    end_index -= 1
                    continue
                elif sum < target:
                    start_index += 1
                    continue
                else:
                    ans.append(start_index)
                    ans.append(end_index)
                    return ans  



"""
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
# Test
sol = Solution()
# nums = [2,7,11,15]
# target = 9

# nums2 = [3, 2, 4]
# target2 = 6
# print(sol.twoSum(nums2, target2))

nums3 = [-1,-2,-3,-4,-5]
target = -8
print(sol.twoSum2(nums3, target))
