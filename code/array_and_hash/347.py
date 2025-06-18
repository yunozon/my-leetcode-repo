from collections import defaultdict

class Solution:
    def topKFrequent_My_Ans(self, nums, k):
        dict = defaultdict(int)
        ans = []
        for num in nums:
            dict[num] += 1 # numをkeyにして何回あるかを辞書に格納

        sorted_dict = sorted(dict.items(), key=lambda x:x[1], reverse=True) # value(回数)の値が大きい順に並び替え
        
        for i in range(k):
            ans.append(sorted_dict[i][0])
        print(ans)
        return ans


sol = Solution()
nums1 = [1]
nums2 = [3, 2, 1, 2, 1, 1, 4, 5, 4]
k1 = 1
k2 = 3
sol.topKFrequent(nums1, k1)
sol.topKFrequent(nums2, k2)

