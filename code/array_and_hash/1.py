# Two sum
from time import time
class Solution:
    def twoSum(self, nums, target):
        # brute force
        n = len(nums)
        ans = []
        for i in range(n-1):
            for j in range(i+1, n):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]
        return []
    
    def twoSum2(self, nums, target):
        """
        Hashmapを使って一度のパスで解く
        計算量はO(n)

        nums = [2,7,11,15], target = 9
        hashmap = {2:0, 7:1, 11:2, 15:3}
        i = 0, num = 2, complement = 7, hashmap[2] = 0
        i = 1, num = 7, complement = 2, hashmap[7] = 1
        return [0, 1]
        """
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num # 補数を計算
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i # numがkey, iがvalue (iはindexを表す)
        return []

    def twoSum3(self, nums, target):
        """
        Hashmapを使って2度のパスで解く
        1回目は、すべての要素をhashmapに保存
        2回目は、各要素の補数を計算してhashmapから探す
        計算量はO(n)
        """
        hashmap = {}
        # 一度目のパスでhashmapを作成
        # numsの各要素をkey, そのindexをvalueとして保存
        for i, num in enumerate(nums):
            hashmap[num] = i

        # 二度目のパスで補数を計算
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap and hashmap[complement] != i: # 同じ要素を使わないようにチェック
                return [i, hashmap[complement]]
        return []
    
    def twoSum4(self, nums, target):
        """
        ソートして2ポインタを使う方法
        計算量はO(n log n) (ソートのため)
        nums = [2,7,11,15], target = 9
        left = 0, right = 3
        nums[left] + nums[right] = 2 + 15 = 17 > 9
        このとき、targetよりも大きいので、rightを1つ左に移動
        """

        # 元のインデックスを保持する
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        indexed_nums.sort() # 値でソート

        left, right = 0, len(nums) - 1
        while left < right:
            current_sum = indexed_nums[left][0] + indexed_nums[right][0]
            if current_sum == target:
                return [indexed_nums[left][1], indexed_nums[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []
    
    def twoSum5(self, nums, target):
        """
        辞書のget()メソッドを使った方法
        計算量はO(n)
        """
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            complement_index = seen.get(complement) # getメソッドを使うことで、キーが存在しない場合はNoneを返す。キーが存在する場合はその値を返す。
            if complement_index is not None:
                return [complement_index, i]
            seen[num] = i
        return []

def Test():
    sol = Solution()
    test_cases = [
        [[2, 7, 11, 15], 9, [0, 1]], # [nums, target, expected_output]
        [[3, 2, 4], 6, [1, 2]],
        [[-2, -3, -4, -5, -6], -11, [3, 4]],
    ]

    methods = [
        sol.twoSum,
        sol.twoSum2,
        sol.twoSum3,
        sol.twoSum4,
        sol.twoSum5
    ]
    for method in methods:
        start_time = time() # 計測開始
        print(f"Testing {method.__name__}")
        for nums, target, expected in test_cases:
            result = method(nums, target)
            print(f"Input: nums = {nums}, target = {target}")
            print(f"Expected: {expected}, Got: {result} Result: {'Pass' if result == expected else 'Fail'}")
        end_time = time()    
        elapsed_time = end_time - start_time
        print(f"Elapsed time for {method.__name__}: {elapsed_time:.6f} seconds")
        print("=" * 40)


if __name__ == "__main__":
    Test()
